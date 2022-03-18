from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import json
import time

PATH = "D:\POLBAN\Semester 2\Proyek 1\Scrapping2\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://music.apple.com/us/playlist/top-100-indonesia/pl.2b7e089dc9ef4dd7a18429df9c6e26a3")
i = 1
songlist = []
for list in driver.find_elements(By.CLASS_NAME, "songs-list-row songs-list-row--web-preview web-preview songs-list-row--two-lines songs-list-row--song"):
    print(list.text)
    time.sleep(0.5)
    #for image in list.find_elements(By.CLASS_NAME, "o-chart-results-list__item"):
        #for img1 in image.find_elements(By.CLASS_NAME, "lrv-a-crop-1x1 a-crop-67x100@mobile-max"):
   # for img in list.find_elements(By.TAG_NAME, "img"):
        #print(img.get_attribute("src"))
            # urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
            # i += 1
                
                #songlist.append(
                #   {"No": list.text.split("\n")[0],
                # "Judul": list.text.split("\n")[1],
                # "Last week": list.text.split("\n")[2],
                # "Peak Post": list.text.split("\n")[3],
                # "Wks on chart": list.text.split("\n")[4],
                # "Image": img.get_attribute("src")
                # }
            # )

hasil_scrapping = open("hasilscrapping.json", "w")
json.dump(songlist, hasil_scrapping, indent=6)
hasil_scrapping.close()
driver.quit()