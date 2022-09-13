import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("public/images/i1.jpg")

imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.subplot(2,2,1)
plt.imshow(imgRGB)
plt.title("normal")

gaussian = cv.GaussianBlur(img,(5,5),0) 

gaussianRGB = cv.cvtColor(gaussian,cv.COLOR_BGR2RGB)
plt.subplot(2,2,2)
plt.imshow(gaussianRGB)
plt.axis('off')
plt.title("gaussian image")

median = cv.medianBlur(img,5)

medianRGB = cv.cvtColor(median,cv.COLOR_BGR2RGB)
plt.subplot(2,2,3)
plt.imshow(medianRGB)
plt.axis('off')
plt.title("median blur image")

plt.waitforbuttonpress(0)

print(img)
print(np.float32(img))
