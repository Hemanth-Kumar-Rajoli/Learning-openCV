import cv2 as cv
capture = cv.VideoCapture(0)
capture.set(3,1080) #for width
capture.set(4,720) #for height
#10 for brightness
while True:
    isTrue,frame = capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
capture.release()