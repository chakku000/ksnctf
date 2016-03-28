#coding: utf-8
import numpy as np
import cv2

#create image
img = np.zeros((31,31,3),np.uint8)

#load file
file = open('in.txt').readlines()

for i in range(31):
    for j in range(31):
        img[i][j] = int(file[i][j])*255

#large size
#img_large = np.zeros((310,310,3),np.uint8)

hight = img.shape[0]
width = img.shape[1]

img_large = cv2.resize(img,(hight*5,width*5))

cv2.imwrite('img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


