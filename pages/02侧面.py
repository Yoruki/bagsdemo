import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd

def drawline():
    data = pd.read_csv('side/whitepixels.csv')
    st.line_chart(data)

st.subheader('侧视图')

# 播放视频
uploaded_file2 = st.file_uploader('选择侧面视频')  # return type: BytesIO
if uploaded_file2 is not None:
    estimate = uploaded_file2.read()
    st.video(estimate)

if st.sidebar.button('提取关键帧'):

    # 计算白色像素点提取关键帧
    drawline()

    # 关键帧
    image = Image.open('side/3.test_result5.jpg')
    st.image(image, caption='关键帧')

    # 关键帧二值化
    image_close = Image.open('side/4.img_open_thresh.jpg')
    st.image(image_close, caption='关键帧二值化')

    # 关键帧二值化抠图
    image_kotuclose = Image.open('side/5.clean.jpg')
    st.image(image_kotuclose, caption='关键帧二值化抠图')

    # 关键帧抠图
    image_kotu = Image.open('side/6.kotu.jpg')
    st.image(image_kotu, caption='关键帧抠图')




