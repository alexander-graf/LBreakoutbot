import numpy as np
import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)
print(type(events))

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',  ' + str(y)
        cv.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 1 )
        cv.imshow('image', img)

img = np.zeros([512, 512, 3], np.uint8)
cv.imshow('image', img)

cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()

