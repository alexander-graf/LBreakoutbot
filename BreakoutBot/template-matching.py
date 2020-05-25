import time
import mss
import cv2
import numpy as np


# Schläft ein bisschen
# Zeit zum Einschalten von LBreakout
time.sleep(2)

# Grab screen area of LBreakout
# nimmt den Teilbereich rechts oben auf dem Hauptbildschirm
def erkenneball():
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 1290, "width": 600, "height": 500}
        #while "Screen capturing":
            #Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        # Display the picture
        #cv2.imshow("OpenCV/Numpy normal", img)   #zeigt das Spiel permanent in einem Fenster
        #cv2.waitKey(0)

    # Ein Bild wurde erfolgreich geschossen
    # Jetzt kommt der Vergleich mit ball.jpg


    #img = cv2.imread("/home/alexander/Python-Eigene/BreakoutBot/spielfeld.jpg")
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("/home/alexander/Python-Eigene/BreakoutBot/ball.jpg", 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED )
    #print(res)
    threshold = 0.99;
    loc = np.where(res >= threshold)
    #print(loc)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        print("Koordinaten: ", pt[0], pt[1])
        pt =[]   # leert die Liste wieder
    #cv2.imshow("img", img)   # zeichnet einen Rahmen um den gefundenen Ball. Muss nicht mehr angezeigt werden. Ich brauche nur die x, y Werte des Balls

#Hauptprogramm sozusagen :-)
for i in range(1,1000):
    erkenneball()

cv2.waitKey(0)
cv2.destroyAllWindows()

