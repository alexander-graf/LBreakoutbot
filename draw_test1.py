import numpy as np
import cv2

#img = cv2.imread ('kleinesFeldMitBall.png', 1)
img = np.zeros([300, 500, 3], np.uint8)

img = cv2.line(img, (0,0), (25,25), (0, 0, 255), 1)

img = cv2.rectangle(img, (1, 1), (30, 30), (255, 0, 0), 5)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

