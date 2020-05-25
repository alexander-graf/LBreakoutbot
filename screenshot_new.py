import pyautogui
import cv2
import numpy as np

a = 1
while a<2:
    image = pyautogui.screenshot(region=(1280,0,1920,500))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    a += 1
    print(a)


    cv2.imshow("image", image)


cv2.waitKey(0)
cv2.destroyAllWindows()

