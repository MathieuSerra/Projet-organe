print ('hello world')

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(1)
img=cv.imread('fluoro_1.jpg')
while True:
    ret,frame=cap.read()
    width=480
    height=480
    sframe=frame[0:height, 0:width]
    simg=img[0:height,0:width]
    
    gray=cv.cvtColor(sframe, cv.COLOR_BGR2GRAY)
    #f_gray=cv.medianBlur(frame,3)

    _, th1=cv.threshold(gray, np.mean(gray)-30, 255, cv.THRESH_BINARY_INV)
    #ret, th=cv.threshold(img_gray, 0,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    #kernel=np.ones((3,3), np.uint8)
    #morpho=cv.morphologyEx(th1, cv.MORPH_CLOSE, kernel)

    sum2=cv.bitwise_and(sframe,sframe,mask=th1)
    sum2=cv.bitwise_not(sum2)-90
    final=cv.addWeighted(simg,0.9,sum2,0.4,0)
    #final=cv.cvtColor(final,cv.COLOR_BGR2GRAY)

    cv.imshow('frame',final)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()