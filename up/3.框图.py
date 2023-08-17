import cv2
import numpy as np
from skimage import morphology
kernel = np.ones((1, 5), np.uint8)
img = cv2.imread("image_filtered.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# print(binary)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, anchor=(2, 0), iterations=5)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cnt=contours[0]
a=cv2.contourArea(cnt)
print(a)
cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow("img", img)
cv2.waitKey(0)
