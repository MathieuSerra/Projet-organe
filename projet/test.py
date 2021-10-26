print ('hello world')

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

currentFrame=0
while(True):
    ret, frame = cap.read()
    frame = cv.flip(frame,1)
    #ret,mask = cv.threshold(frame,30,255,cv.THRESH_BINARY)
    frame=  cv.bitwise_not(frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow('frame',gray)
    if cv.waitKey(0) & 0xFF == ord('q'):
       break

    currentFrame += 1

cap.release()
cv.destroyAllWindows()