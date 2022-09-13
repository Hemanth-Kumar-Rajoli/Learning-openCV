import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("public/images/fruits.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)

canny = cv.Canny(blur,150,175)

counters,hyrarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(counters)} this many counters found!')
cv.imshow("gray",gray)
cv.imshow('blur',blur)
cv.imshow("canny",canny)
cv.imshow("original",img)

blank = np.zeros(img.shape,'uint8')
cv.drawContours(blank,counters,-1,(0,255,0),1)

cv.imshow('counters',blank)
cv.waitKey(0)
cv.destroyAllWindows()