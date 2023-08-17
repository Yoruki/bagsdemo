# edges = cv.Canny( image, threshold1, threshold2[, apertureSize[, L2gradient]])
# edges 为计算得到的边缘图像。
# image 为 8 位输入图像。
# threshold1 表示处理过程中的第一个阈值。
# threshold2 表示处理过程中的第二个阈值。
# apertureSize 表示 Sobel 算子的孔径大小。
# L2gradient 为计算图像梯度幅度（gradient magnitude）的标识。其默认值为 False。
# 如果为 True，则使用更精确的 L2 范数进行计算（即两个方向的导数的平方和再开方），否则使用 L1 范数（直接将两个方向导数的绝对值相加）。
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('kotu.jpg')
kernel = np.ones((10,10),np.uint8)
edges_orin = cv2.Canny(img,10,100,apertureSize=3)
edges=cv2.dilate(edges_orin,kernel)   #膨胀
edges2_orin = cv2.Canny(img,50,200,apertureSize=5)
edges2=cv2.dilate(edges2_orin,kernel)  #膨胀

plt.subplot(131),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image1'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(edges2,cmap = 'gray')
plt.title('Edge Image2'), plt.xticks([]), plt.yticks([])
plt.show()
