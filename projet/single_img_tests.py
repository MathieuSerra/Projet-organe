import numpy as np
import cv2 as cv

max_value=255
max_type=4
max_binary_value=255
window_name='Threshold Demo'

img2=cv.imread('fluoro_1.jpg')
img=cv.imread('test_image.jpg')-50
img=img[0:512, 0:512]
print (img2.shape)
img_name=img
img_gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray=cv.medianBlur(img_gray,3)
_, th1=cv.threshold(img_gray, np.mean(img_gray)-45, 255, cv.THRESH_BINARY)
#th1=cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 8)
#th2=cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
ret, th=cv.threshold(img_gray, 0,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
#sum1=cv.bitwise_or(th1,th2)
#_, th= cv.threshold(img_gray,80,255, cv.THRESH_BINARY)
#cv.imshow('th1', sum1)
#cv.imshow('th2',sum1)

#Canny edge test
edges=cv.Canny(image=img, threshold1=45, threshold2=65)
kernel=np.ones((3,3), np.uint8)
edge_eroded=cv.erode(edges,kernel,iterations=1)
edge_dilated=cv.dilate(edges,kernel,iterations=1)
edge_closed=cv.morphologyEx(edges,cv.MORPH_CLOSE, kernel)

img_floodfill=edge_closed.copy()
h,w=edge_closed.shape[:2]
contours=cv.findContours(edge_closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contours=contours[0] if len(contours)==2 else contours[1]
bigcontour=max(contours, key=cv.contourArea)
result=np.zeros_like(edge_closed)
cv.drawContours(result, [bigcontour],0,(255,255,255),cv.FILLED)



#mask=np.zeros((h+2,w+2),np.uint8)
#img_floodfill=img_floodfill.astype('uint8')
#cv.floodFill(edge_closed,mask,(100,100),255)
#img_out=edge_closed | img_floodfill

#cv.imshow('Canny',edges)
#cv.imshow('erosion',edge_eroded)
#cv.imshow('daltion',edge_dilated)
cv.imshow('morph',result)

cv.waitKey(0)
#kernel=np.ones((3,3), np.uint8)
#morpho=cv.morphologyEx(th1, cv.MORPH_CLOSE, kernel)
#sum2=cv.bitwise_or(img,img,mask=th1)
#sum3=cv.bitwise_or(img,img,mask=morpho)
#final=cv.addWeighted(img2,0.7,sum2,0.9,0)
#final1=cv.addWeighted(img2,0.7,sum3,0.9,0)
#sum3=cv.bitwise_and(sum2,img2)
#cv.imshow('test',sum2)
#cv.imshow('test1',final)
#cv.imshow('test2',final1)

#cv.waitKey()