import cv2
import numpy as np
img_fia = cv2.imread("test_result5.jpg",0)
img_trh= cv2.imread("5.clean.jpg", 0)
img_fia = cv2.resize(img_fia, (1200,900))
for i in range(900):
    for j in range(1200):
        if img_trh[i,j]==0:
            img_fia[i,j]=0
# print(img_trh.shape[0])
# print(img_trh.shape[1])
# print(img_fia.shape[0])
# print(img_fia.shape[1])
cv2.imwrite("6.kotu.jpg", img_fia)
cv2.imshow('img',img_fia)
cv2.waitKey(0)