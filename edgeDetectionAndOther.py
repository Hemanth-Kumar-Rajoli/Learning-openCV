import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("public/images/fruits.jpg")
imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.subplot(2,2,1)
plt.imshow(imgRGB)
plt.axis('off')
plt.title("original")

#canny Edge detection

canny = cv.Canny(img,150,175)

cannyRGB = cv.cvtColor(canny,cv.COLOR_BGR2RGB)
plt.subplot(2,2,2)
plt.imshow(cannyRGB)
plt.axis('off')
plt.title("canny")


#dilution(increases the border weight)

dilate = cv.dilate(canny,(7,7),iterations=3)

dilateRGB = cv.cvtColor(dilate,cv.COLOR_BGR2RGB)
plt.subplot(2,2,3)
plt.imshow(dilateRGB)
plt.axis('off')
plt.title("dilate")

#er0iding (opposite to the dilution)
erode = cv.erode(dilate,(7,7),iterations=3)

erodeRGB = cv.cvtColor(erode,cv.COLOR_BGR2RGB)
plt.subplot(2,2,4)
plt.imshow(erodeRGB)
plt.axis('off')
plt.title("erode")

plt.waitforbuttonpress(0)
