import cv2
import matplotlib.pyplot as plt
import numpy as np

image1 = cv2.imread("videotoframe\\frame14.jpg",0)
image2 = cv2.imread('videotoframe\\frame0.jpg',0)

des = np.zeros((3000,4096), np.uint8)
for i in range(3000):
    for j in range(4096):
        if abs(image1[i,j] != image2[i,j]):
            des[i,j] = image1[i,j]


pixel_diff = cv2.absdiff(image1, image2)
cv2.imwrite("3.test_result4.jpg",pixel_diff)
cv2.imwrite("3.test_result5.jpg",des)
plt.imshow(pixel_diff, cmap='gray')
plt.imshow(des, cmap='gray')
plt.show()