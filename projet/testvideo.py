print ('hello world')

import cv2 as cv
import numpy as np
import time
cap = cv.VideoCapture('video-standard.mp4')
img2=cv.flip(cv.transpose(cv.imread('fluoro_2.jpg')),flipCode=0)
new_frame_time=0
prev_frame_time=0
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
img2=cv.resize(img2,(640,480),interpolation=cv.INTER_AREA)
out=cv.VideoWriter('Test_fluoroscopie02_22-04-05-02.mp4',cv.VideoWriter_fourcc(*'MP4V'),20,(frame_width,frame_height))
i=1
mean=0

while (cap.isOpened()):
    ret,frame=cap.read()
    if frame is None:
        break
    print(frame.shape)
    img=frame
    #img=cv.pyrDown(frame)
    #img=cv.pyrDown(img)
    
    #TEST1
    #twoDimage=img[:,:,0].reshape((-1,1))
    #twoDimage=np.float32(twoDimage)+50
    #criteria=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,2,1.0)
    #K=3
    #attempts=3
    #ret, label, center=cv.kmeans(twoDimage,K,None,criteria,attempts,cv.KMEANS_PP_CENTERS)
    #center=np.uint8(center)
    #res=center[label.flatten()]
    #result_image1=res.reshape((img[:,:,0].shape))


    #edges=cv.Canny(image=img[:,:,0], threshold1=30, threshold2=100)
    #kernel=np.ones((3,3), np.uint8)
    #result_image=cv.morphologyEx(edges,cv.MORPH_CLOSE, kernel)

    if (i%40==0):
        mean=np.mean(img[:,:,0])
    i+=1
    print (mean)
    if (mean==0):
        ret,th=cv.threshold(img[:,:,0],220,255,cv.THRESH_BINARY)
        ret,mask=cv.threshold(img[:,:,0],130,255,cv.THRESH_BINARY)
        img_masked=cv.bitwise_or(img[:,:,0],mask)
        heart=mask-th
        heart[heart==255]=160
    else:
        ret,th=cv.threshold(img[:,:,0],142+mean,255,cv.THRESH_BINARY)
        ret,mask=cv.threshold(img[:,:,0],52+mean,255,cv.THRESH_BINARY)
        img_masked=cv.bitwise_or(img[:,:,0],mask)
        heart=mask-th
        heart[heart==255]=30+mean
    

    new_img=cv.bitwise_not(cv.bitwise_or(img[:,:,0],(th)))
    #new_img=cv.blur(new_img,(5,5))


    #gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)+50
    #th=cv.blur(th,(5,5))
    #result_image=cv.bitwise_or(gray,th)
    #result_image=cv.bitwise_not(result_image)
    #result_image=cv.resize(cv.bitwise_not(result_image),(640,360),interpolation=cv.INTER_AREA)
    
    #row,col=result_image.shape
    #mean=0
    #var=0.5
    #sigma=var**0.5
    #gauss=np.random.normal(mean,sigma,(row,col))
    #gauss=gauss.reshape(row,col)



    final=cv.addWeighted(new_img,0.4,cv.cvtColor(img2,cv.COLOR_BGR2GRAY),0.6,0.0)
    final=cv.resize(final,(frame_width,frame_height),interpolation=cv.INTER_AREA)
    #fpsText = "FPS: " + str(fps)
    #cv.putText(final, fpsText, (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3, cv.LINE_AA)
    final=cv.cvtColor(final,cv.COLOR_GRAY2BGR)
    out.write(final)
    if (mean!=0):
        cv.imshow('frame',mask)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
out.release
cv.destroyAllWindows()