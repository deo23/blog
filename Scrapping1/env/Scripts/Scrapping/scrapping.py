# import package requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

# request ke website
page = requests.get("https://republika.co.id/")

#ekstrak konten menjadi objek  BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser');
print("Menampilkan objek html")
print("=======================")
print(obj)

print("\nMenampilkan title browser dengan tag")
print("========================================")
print(obj.title)

print("\nMenampilkan title browser tanpa tag")
print("========================================")
print(obj.title.text)

print("\nMenampilkan semua tag")
print("========================")
print(obj.find_all('h2'))

print("\nMenampilkan semua teks")
print("========================")
for headline in obj.find_all('h2'):
    print(headline.text)

print("\nMenampilkan berita terkini berdasarkan div class")
print("=============================================")
print(obj.find_all('div',class_='teaser_conten1_center'))

print("\nMenampilkan semua teks terkini")
print("==================================")
for headline in obj.find_all('div',class_='teaser_conten1_center'):
    print(headline.find('h2').text)

print('\nMenampilkan kategori')
print('========================')
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

print('\nMenampilkan waktu publish')
print('========================')
for publish in obj.find_all('div',class_='date'):
        print(publish.text)
        x = datetime.now()
        #print(x.strftime("%d/%m/%y  %X"))

print('\nMenyimpan berita terkini pada json')
print('====================================')
data = []
x = datetime.now()
f = open('D:\POLBAN\Semester 2\Proyek 1\Scrapping1\\terkini.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktu_publish":publish.find('div',class_='date').text,
    "waktu_scraping":x.strftime("%d-%m-%Y %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()