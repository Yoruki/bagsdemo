import cv2
import matplotlib.pyplot as plt
import pandas as pd

y = []
x = []

videoCapture = cv2.VideoCapture()
videoCapture.open('../video/D4.avi')
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
# print(frames)
for i in range(1, 401, 2):
    ret, frame = videoCapture.read()
    # ret, thresh = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
    a = len(frame[frame > 110])
    print(a)
    # cv2.imwrite("frames\\frame%d.jpg" % (i), frame)
    x.append([i])
    y.append([a])

    # print(y)
    # print(x)
    # plt.plot(x, y)
    # plt.show()

data = pd.DataFrame(y)
data.to_csv('whitepixels.csv',index=False)

