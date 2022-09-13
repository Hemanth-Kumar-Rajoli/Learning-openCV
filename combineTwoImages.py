import cv2 as cv
import numpy as np

img1 = cv.imread("./public/images/i1.jpg")
img2 = cv.imread("./public/images/i3.jpg")

# mixed = cv.addWeighted(img1,0.5,img2,0.5,0.0)
print(img1.size)
img1 = cv.resize(img1,(img1.shape[1]//2,img1.shape[0]//2))
img2 = cv.resize(img2,(img2.shape[1]//2,img2.shape[0]//2))
# cv.addWeighted(img1,alpha,img2,beta,game) gama is for brightness(my guess)
mixed = cv.addWeighted(img1,1,img2,1,0.0)
cv.imshow("add weighted",mixed)

cv.waitKey(0)

cv.destroyAllWindows()


