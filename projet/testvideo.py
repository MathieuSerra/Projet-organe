print ('hello world')

import cv2 as cv
import numpy as np
import time
cap = cv.VideoCapture('testvideo4.mp4')
img2=cv.flip(cv.transpose(cv.imread('fluoro_2.jpg')),flipCode=0)
#img2=img2[0:540,0:960]
img2=cv.resize(img2,(640,360),interpolation=cv.INTER_AREA)
new_frame_time=0
prev_frame_time=0

while True:
    ret,frame=cap.read()
    new_frame_time = time.time()
    fps = int(1/(new_frame_time-prev_frame_time))
    prev_frame_time = new_frame_time
    #img=frame
    img=cv.pyrDown(frame)
    #img=cv.pyrDown(img)
    
    #TEST1
    twoDimage=img[:,:,0].reshape((-1,1))
    twoDimage=np.float32(twoDimage)
    criteria=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,2,1.0)
    K=3
    attempts=3
    ret, label, center=cv.kmeans(twoDimage,K,None,criteria,attempts,cv.KMEANS_PP_CENTERS)
    center=np.uint8(center)
    res=center[label.flatten()]
    result_image1=res.reshape((img[:,:,0].shape))


    #edges=cv.Canny(image=img[:,:,0], threshold1=30, threshold2=100)
    #kernel=np.ones((3,3), np.uint8)
    #result_image=cv.morphologyEx(edges,cv.MORPH_CLOSE, kernel)


    ret,th=cv.threshold(result_image1,150,255,cv.THRESH_BINARY)
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)+50
    th=cv.blur(th,(5,5))
    result_image=cv.bitwise_or(gray,th)
    result_image=cv.bitwise_not(result_image)
    #result_image=cv.resize(cv.bitwise_not(result_image),(640,360),interpolation=cv.INTER_AREA)
    
    #row,col=result_image.shape
    #mean=0
    #var=0.5
    #sigma=var**0.5
    #gauss=np.random.normal(mean,sigma,(row,col))
    #gauss=gauss.reshape(row,col)



    final=cv.addWeighted(result_image,0.4,cv.cvtColor(img2,cv.COLOR_BGR2GRAY),0.6,0.0)
    fpsText = "FPS: " + str(fps)
    cv.putText(final, fpsText, (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3, cv.LINE_AA)
  

    cv.imshow('frame',final)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()