print ('hello world')

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(1)
img2=cv.imread('fluoro_1.jpg')
img2=img2[0:512,0:350]
img2=cv.resize(img2,(640,480),interpolation=cv.INTER_AREA)
while True:
    ret,frame=cap.read()
    img=frame
    print(frame.shape)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    print(img2.shape)
    #TEST1
    twoDimage=img[:,:,0].reshape((-1,1))
    twoDimage=np.float32(twoDimage)
    print(twoDimage.shape)
    criteria=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,2,1.0)
    K=3
    attempts=3
    ret, label, center=cv.kmeans(twoDimage,K,None,criteria,attempts,cv.KMEANS_PP_CENTERS)
    center=np.uint8(center)
    res=center[label.flatten()]
    result_image=res.reshape((img[:,:,0].shape))
    #result_image=cv.cvtColor(result_image, cv.COLOR_RGB2GRAY)
    ret,th=cv.threshold(result_image,100,255,cv.THRESH_BINARY)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)+50
    ret, result=cv.threshold(cv.bitwise_or(gray,th),253,255,cv.THRESH_TOZERO_INV)
    final=cv.addWeighted(result,0.6,cv.cvtColor(img2,cv.COLOR_BGR2GRAY),0.4,0.0)

    cv.imshow('frame',result_image)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()