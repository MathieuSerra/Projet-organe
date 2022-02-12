print ('hello world')

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
img2=cv.imread('fluoro_1.jpg')
img2=img2[0:512,0:350]
img2=cv.resize(img2,(320,240),interpolation=cv.INTER_AREA)

while True:
    ret,frame=cap.read()
    img=cv.pyrDown(frame)

    print(img.shape)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
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


    #edges=cv.Canny(image=img[:,:,0], threshold1=30, threshold2=100)
    #kernel=np.ones((3,3), np.uint8)
    #result_image=cv.morphologyEx(edges,cv.MORPH_CLOSE, kernel)


    ret,th=cv.threshold(result_image,150,255,cv.THRESH_BINARY)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)+50
    ret, result_image=cv.threshold(cv.bitwise_or(gray,th),253,255,cv.THRESH_TOZERO_INV)
    final=cv.addWeighted(result_image,0.6,cv.cvtColor(img2,cv.COLOR_BGR2GRAY),0.4,0.0)
    final=cv.resize(final,(640,480),interpolation=cv.INTER_AREA)

    cv.imshow('frame',final)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()