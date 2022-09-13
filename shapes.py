import cv2 as cv
import numpy as np

black = np.zeros((500,500,3),dtype='uint8')
cv.imshow('black',black)
black[200:300,300:400] = [255,255,255]

cv.rectangle(black,(0,0),(255,255),(0,255,0),thickness=2) #if thickness is -1 then it will the area
cv.putText(black,'Hello',(250,250),cv.FONT_HERSHEY_TRIPLEX,3.0,(255,0,0),3)
cv.imshow('green',black)
print(black[:])
cv.waitKey(0)