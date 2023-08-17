import cv2
import numpy as np
img_fia = cv2.imread("input.jpg",0)
img_trh= cv2.imread("image_filtered.jpg",0)

for i in range(1080):
    for j in range(1920):
        if img_trh[i,j]==0:
            img_fia[i,j]=0
# print(img_trh.shape[0])
# print(img_trh.shape[1])
# print(img_fia.shape[0])
# print(img_fia.shape[1])
cv2.imshow('img',img_fia)
cv2.waitKey(0)