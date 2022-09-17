import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("public/images/fruits.jpg")

#normal blur takes center as average of kernal matrix sized
blur = cv.blur(img,(7,7))
cv.imshow("blur",blur)

#gausian blur
#every pixel has defined some wieght and takes that much and average them

gausian = cv.GaussianBlur(img,(7,7),0)
cv.imshow("gaussina",gausian)

#median blur
#more good to remove salt and pepper type of noises but in smaller case

medain = cv.medianBlur(img,7)
cv.imshow("medain",medain)

cv.imshow("original",img)
cv.waitKey(0)
cv.destroyAllWindows()