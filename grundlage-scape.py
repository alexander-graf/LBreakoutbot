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
driver.get("http://www.lotuscafe.de")
assert "LotusCafe" in driver.title
elem = driver.find_element_by_id("loginbox_username")
elem.send_keys(user)
elem = driver.find_element_by_id("loginbox_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
#driver.close()


#URL eingeben

driver.get("https://lotuscafe.de/index.php?m=member_profile&p=profile&id=1119696")

#Schleife

for i in range(1125000, 0,-1):
    #time.sleep(5)
    id = str(i)
    driver.get("https://lotuscafe.de/index.php?m=member_profile&p=profile&id=" + id )
    print(id)


