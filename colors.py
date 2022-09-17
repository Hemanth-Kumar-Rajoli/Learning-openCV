from heapq import merge
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("public/images/fruits.jpg")

b,g,r = cv.split(img)
merged = cv.merge([b,g,r])

cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
cv.imshow("merged",merged)


cv.imshow("original",img)
cv.waitKey(0)
cv.destroyAllWindows() 