import numpy as np
import cv2 as cv2
import matplotlib as plt

window_name=' Demo'

img_fluoro=cv2.imread('Test_CNR_SNR.png')
img_normal=cv2.imread('test_normal.png')
img_normal=cv2.cvtColor(img_normal,cv2.COLOR_BGR2GRAY)

print(img_fluoro.shape)
print(img_normal.shape)

img_fluoro=cv2.rectangle(img_fluoro,(235,205),(250,220),(255,0,0),2) #roi 
img_fluoro=cv2.rectangle(img_fluoro,(280,220),(330,270),(0,0,255),2) #bckg alginate
img_fluoro=cv2.rectangle(img_fluoro,(380,220),(530,370),(0,255,0),2) #gros bckg
gray_fluoro=cv2.cvtColor(img_fluoro,cv2.COLOR_BGR2GRAY)
CNR=abs((np.mean(gray_fluoro[235:250,205:220])-np.mean(gray_fluoro[380:530,220:370])))/np.std(gray_fluoro[380:530,220:370])
SNR=20*np.log((np.mean(gray_fluoro[235:250,205:220]))/(np.std(gray_fluoro[380:530,220:370])))
cv2.imshow(window_name,img_fluoro)

print('Le CNR est de : ', CNR, ' pour l''image choisie')
print('Le SNR est de : ', SNR, ' pour l''image choisie')
cv2.waitKey(0)
cv2.destroyAllWindows()
#img_fluoro=cv2.cvtColor(img_fluoro,cv2.COLOR_BGR2GRAY)

