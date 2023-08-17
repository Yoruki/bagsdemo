import numpy as np
import cv2 as cv

# 加载图片
img = cv.imread("img_close1.jpg")
# 灰度化
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret, thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
# 寻找连通域
num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(thresh, connectivity=8)

# 计算平均面积
areas = list()
for i in range(num_labels):
    areas.append(stats[i][-1])
    print("轮廓%d的面积:%d" % (i, stats[i][-1]))

area_avg = np.average(areas[1:-1])
print("轮廓平均面积:", area_avg)

# 筛选超过平均面积的连通域
image_filtered = np.zeros_like(img)
for (i, label) in enumerate(np.unique(labels)):
    # 如果是背景，忽略
    if label == 0:
        continue
    if stats[i][-1] > area_avg :
        image_filtered[labels == i] = 255

cv.imshow("image_filtered", image_filtered)
cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()




