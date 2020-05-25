from selenium import webdriver
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)


import time
from selenium.webdriver.common.keys import Keys
user = "GuterKuesser"
pwd = "lutschmeinei"
#driver = webdriver.Firefox()
driver.get("http://www.esoterik-freunde.de/L/?uid=516896&cp=e0cb06870c597ff54cd456929ace421a")


#URL eingeben

driver.get("https://www.esoterik-freunde.de/view_profile.php?uid=1")

#Schleife

for i in range(40000,200000,1):
    #time.sleep(5)
    id = str(i)
    driver.get("https://www.esoterik-freunde.de/view_profile.php?uid=" + id )
    print(id)


