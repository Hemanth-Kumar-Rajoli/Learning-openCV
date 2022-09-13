import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("public/images/fruits.jpg")

def trasulate(img,x,y):
    transM = np.float32([[1,0,x],[0,1,y]])
    return cv.warpAffine(img,transM,(img.shape[1],img.shape[0]))
def rotate(img,angle,rotationPoint=None):
    if(rotationPoint is None):
        rotationPoint = (img.shape[0]//2,img.shape[1]//2)
    rotationMa = cv.getRotationMatrix2D(rotationPoint,angle,1.0)
    return cv.warpAffine(img,rotationMa,(img.shape[1],img.shape[0]))
cv.imshow("original",img)
cv.imshow("fliped",cv.flip(img,1))#1 is horzantal flip 0 vertical flip -1 is both horizantal and vertical flip
cv.imshow("transformed image",trasulate(img,100,100))
cv.imshow("rotated image",rotate(img,45))
cv.waitKey(0)
cv.destroyAllWindows()