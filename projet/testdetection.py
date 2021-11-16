print ('hello world')

import cv2 as cv
import numpy as np
#cap0=cv.VideoCapture(1)
cap = cv.VideoCapture(1)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_eye.xml')

while True:
    ret,frame=cap.read()
    #width=int(cap.get(3))
    #height=int(cap.get(4))

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),5)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex, ey,ew,eh) in eyes:
            cv.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh),(0,255,0),5)



    #ret0,frame0=cap0.read()
    #gray1 = cv.resize(gray1,(0,0),fx=0.5,fy=0.5)
    #small_frame0 = cv.resize(frame0,(0,0),fx=0.5,fy=0.5)
    #inverted = cv.bitwise_not(small_frame0)
    #gray2 = cv.cvtColor(inverted, cv.COLOR_BGR2GRAY)

    #image=np.zeros((480,640), np.uint8)
    #image[:height//2,:width//2]=gray1
    #image[height//2:,:width//2]=gray1
    #image[:height//2,width//2:]=gray2
    #image[height//2:,width//2:]=gray2
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

