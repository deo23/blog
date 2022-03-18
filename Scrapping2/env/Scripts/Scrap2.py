from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import json
import time
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

PATH = "D:\POLBAN\Semester 2\Proyek 1\Scrapping2\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/search/title/?companies=co0008693")
i = 1
serieslist = []

while i<=100:
    for top in driver.find_elements(By.CLASS_NAME,'lister-item.mode-advanced'):
        #No
        header = top.find_element(By.CLASS_NAME,'lister-item-header')
        no = header.find_element(By.CLASS_NAME, 'lister-item-index.unbold.text-primary')
        print(no.text)
        
        #Judul    
        judul = header.find_element(By.TAG_NAME,'a')
        print(judul.text)

        #Tahun
        tahun = header.find_element(By.CLASS_NAME, 'lister-item-year.text-muted.unbold')
        print(tahun.text)        

        #Rating
        try:
            rating = top.find_element(By.CLASS_NAME, 'ratings-bar')
            rate = rating.find_element(By.TAG_NAME, 'strong')
            print(rate.text)
        except NoSuchElementException:
            print('No rate')
        
        #Gambar
        image = top.find_element(By.CLASS_NAME, 'lister-item-image')
        img = image.find_element(By.TAG_NAME, 'img')
        print(img.get_attribute("src"))
        #urllib.request.urlretrieve(img.get_attribute("src"),"images/" + str(i)+".png")
        i = i + 1
        
        #Waktu Scrapping
        x = datetime.now()

        time.sleep(0.5)       
        
        serieslist.append(
                            {"No": no.text,
                            "Judul": judul.text,
                            "Tahun": tahun.text,
                            "Rating": rate.text,
                            "Image": img.get_attribute("src"),
                            "waktu_scrapping":x.strftime("%d-%m-%Y %H:%M:%S")
                            }
                        )


    
    try:
        driver.find_element_by_class_name("desc").find_element_by_partial_link_text("Next").click()
    except NoSuchElementException as e:
        break;
hasil_scrapping = open("hasilscrapping.json", "w")
json.dump(serieslist, hasil_scrapping, indent=6)
hasil_scrapping.close()
driver.quit()
    