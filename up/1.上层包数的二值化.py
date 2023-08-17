import cv2
import matplotlib.pyplot as plt
import cv2
import numpy as np
from skimage import morphology
img = cv2.imread('input.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(gray, a, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(gray, 50, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(gray, a, 255, cv2.THRESH_TOZERO_INV)
# cv2.imshow('img',thresh4)
# cv2.waitKey(0)
kernel1 = np.ones((15,15),np.uint8)
kernel2 = np.ones((35,35),np.uint8)
img_open=cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel1)
img_close=cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel2)
img_close1=cv2.morphologyEx(img_close, cv2.MORPH_CLOSE, kernel2)
# ero1=cv2.erode(dil2,kernel)
# ero2=cv2.erode(ero1,kernel)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imshow('img',thresh1)
cv2.waitKey(0)
cv2.imshow('img',img_open)
cv2.waitKey(0)
cv2.imshow('img',img_close1)
cv2.waitKey(0)
