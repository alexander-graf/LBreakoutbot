import pyautogui
import os
import time

pyautogui.PAUSE = 2.5


#LibreOffice Writer öffnen
os.system("/usr/bin/libreoffice --writer /home/alex/test111.ott &")

time.sleep(4)

#pyautogui.typewrite('Hello world!', interval=0.25)



#pyautogui.alert('This is an alert box.') 

#pyautogui.confirm('Shall I proceed?')
 

option = pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C']) 


name = pyautogui.prompt('What is your name?') 

pyautogui.moveTo(100, 150) 

pyautogui.click() 


pyautogui.typewrite(option)
pyautogui.typewrite(name)

pyautogui.typewrite("Fögel mich sö hart ey. Bitch, du geile Sau der Säue")




