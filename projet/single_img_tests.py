import numpy as np
import cv2 as cv
import matplotlib as plt

window_name=' Demo'

img2=cv.imread('fluoro_1.jpg')
img=cv.imread('test_image.jpg')
img=img[0:512, 0:512]
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#img=cv.cvtColor(img, cv.COLOR_BGR2RGB)

#TEST1
twoDimage=img.reshape((-1,3))
twoDimage=np.float32(twoDimage)
print(twoDimage.shape)
criteria=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,2,1.0)
K=2
attempts=3
ret, label, center=cv.kmeans(twoDimage,K,None,criteria,attempts,cv.KMEANS_PP_CENTERS)
center=np.uint8(center)
res=center[label.flatten()]
result_image=res.reshape((img.shape))
result_gray=cv.cvtColor(result_image, cv.COLOR_RGB2GRAY)
ret,th=cv.threshold(result_gray,100,255,cv.THRESH_BINARY_INV)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, result=cv.threshold(cv.bitwise_or(gray,th),253,255,cv.THRESH_TOZERO_INV)
final=cv.addWeighted(result,0.6,cv.cvtColor(img2,cv.COLOR_BGR2GRAY),0.4,0.0)
# print(th.shape)

#OLD version

#gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#_, th1=cv.threshold(gray, np.mean(gray)-20, 255, cv.THRESH_TOZERO)






#TEST2
# img=cv.resize(img,(256,256))
# gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
# _,thresh=cv.threshold(gray,np.mean(gray)-35,255,cv.THRESH_BINARY_INV)
# edges=cv.dilate(cv.Canny(thresh,0,255),None)
# #Detecting/drawing contours
# cnt=sorted(cv.findContours(edges,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)[-2],key=cv.contourArea)[-1]
# mask=np.zeros((256,256),np.uint8)
# masked=cv.drawContours(mask,[cnt],-1,255,-1)
# #segmenting the regions
# dst=cv.bitwise_and(img,img,mask=mask)
# segmented=cv.cvtColor(dst,cv.COLOR_BGR2RGB)
#sucks

#TEST3-thresholding


# #Canny edge test
# edges=cv.Canny(image=img, threshold1=45, threshold2=65)
# kernel=np.ones((3,3), np.uint8)
# edge_closed=cv.morphologyEx(edges,cv.MORPH_CLOSE, kernel)
# #water=cv.watershed(edges,img)

cv.imshow(window_name,result_gray)


cv.waitKey(0)
