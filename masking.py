import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Learning-openCV/public/images/fruits.jpg")

black = np.zeros(img.shape[:2],dtype='uint8')

mask = cv.circle(black.copy(),(img.shape[1]//2,img.shape[0]//2),100,(255,255,255),-1)

maskedImage = cv.bitwise_and(img,img,mask=mask)

cv.imshow("mask",mask)
cv.imshow("maked image",maskedImage)
cv.imshow("original",img)
cv.waitKey(0)
cv.destroyAllWindows()