import cv2
from datetime import datetime



def video_to_frames(path):
    videoCapture = cv2.VideoCapture()
    videoCapture.open(path)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    for i in range(int(frames)):
        ret, frame = videoCapture.read()
        cv2.imwrite("videotoframe\\frame%d.jpg" % (i),frame)

    return


if __name__ == '__main__':
    t1 = datetime.now()  #up_loadvideo就是输入的视频_
    video_to_frames("1.avi")
    t2 = datetime.now()
    print("Time cost = ", (t2 - t1))
    print("SUCCEED !!!")





