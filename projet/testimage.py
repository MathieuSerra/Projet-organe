print ('hello world')

import cv2 as cv
import numpy as np
cap0=cv.VideoCapture(1)
cap = cv.VideoCapture(2)

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    ret0,frame0=cap0.read()
    small_frame = cv.resize(frame,(0,0),fx=0.5,fy=0.5)
    small_frame0 = cv.resize(frame0,(0,0),fx=0.5,fy=0.5)
    image=np.zeros(frame.shape, np.uint8)
    image[:height//2,:width//2]=small_frame0
    image[height//2:,:width//2]=small_frame
    image[:height//2,width//2:]=small_frame
    image[height//2:,width//2:]=small_frame
    font = cv.FONT_HERSHEY_SIMPLEX
    image = cv.putText(image, 'Its you!',(200,height -10),font,2,(255,255,255),5,cv.LINE_AA)
    cv.imshow('frame',image)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

