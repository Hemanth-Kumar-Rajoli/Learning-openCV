import cv2 as cv

img = cv.imread("./public/images/i3.jpg")
cv.resize(img,(480,480))
cv.imshow("iron man",img)
resized = cv.resize(img,(480,480),interpolation=cv.INTER_AREA) #dimension are in the form of width and height
cv.imshow("resized iron man",resized)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("iron man GRAY",gray)
cv.waitKey(0)

