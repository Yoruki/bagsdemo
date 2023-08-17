import cv2
import numpy as np

img_diff=cv2.imread("3.test_result5.jpg",0)
img_diff = cv2.resize(img_diff, (1200,900))
# img = cv2.resize(img_origin, (1200,900))
kernel20 = np.ones((20,20),np.uint8)
kernel40 = np.ones((40,40),np.uint8)
kernel60 = np.ones((60,60),np.uint8)
# ero1=cv2.erode(img_diff,kernel)


img_open=cv2.morphologyEx(img_diff, cv2.MORPH_OPEN, kernel40)######1
# img_open1=cv2.morphologyEx(img_open, cv2.MORPH_OPEN, kernel2)
img_close=cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel40)######2

ret, thresh1 = cv2.threshold(img_close, 15, 255, cv2.THRESH_BINARY)#####3
# ret, thresh2 = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(gray, a, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img_diff, 50, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(gray, a, 255, cv2.THRESH_TOZERO_INV)
# ret, thresh5 = cv2.threshold(ero2, 60, 255, cv2.THRESH_BINARY)

img_open_thresh=cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel60)#####5
# cv2.imwrite("4.img_open_thresh.jpg", img_open_thresh)



cv2.imshow('差图',img_diff)
cv2.waitKey(0)
cv2.imshow('open',img_open)
cv2.waitKey(0)
cv2.imshow('close',img_close)
cv2.waitKey(0)
# cv2.imshow('差图',thresh1)
# cv2.waitKey(0)
# cv2.imshow('差图',thresh4)
# cv2.waitKey(0)
cv2.imshow('os',img_open_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()