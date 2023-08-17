import cv2
import pandas as pd

y = []
x = []

for i in range(85):
    im1=cv2.imread("videotoframe\\frame%d.jpg" % (i))
    ret, thresh3 = cv2.threshold(im1, 100, 255, cv2.THRESH_BINARY)
    a=len(thresh3[thresh3 == 255])
    print(a)

    x.append([i])
    y.append([a])
data = pd.DataFrame(y)
data.to_csv('whitepixels.csv',index=False)







