from urllib.request import urlopen
import os
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium import webdriver
firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)


import time
from selenium.webdriver.common.keys import Keys
user = "GuterKuesser"
pwd = "lutschmeinei"
#driver = webdriver.Firefox()
driver.get("http://www.lotuscafe.de")
assert "LotusCafe" in driver.title
#driver.maximize_window()
elem = driver.find_element_by_id("loginbox_username")
elem.send_keys(user)
elem = driver.find_element_by_id("loginbox_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#driver.close()


#URL eingeben
#https://lotuscafe.de/index.php?m=member_pictures&p=pictures&id=1089365
#driver.get("https://lotuscafe.de/index.php?m=member_profile&p=profile&id=1119696")

#Schleife


#https://lotuscafe.de/index.php?m=member_pictures&p=pictures&id=1124210    mein profil

#for i in range(1124245, 0,-1):
i = 1124210
id = str(i)
driver.get("https://lotuscafe.de/index.php?m=member_pictures&p=pictures&id=" + id )

soup = BeautifulSoup(driver.page_source, 'lxml')

print(id)


for link in soup.find_all('img'):
    ein_link = link.get('src')

    #enthält link "uploads?" dann drucken
    if "picture" in ein_link:
        print (ein_link)


        driver.get(ein_link)
        os.system('wget ' + ein_link)




#konkrete URL Bild laden
#https://lotuscafe.de/media/uploads/picture_1124210og97emc25s5qqyjaoas39.jpg

