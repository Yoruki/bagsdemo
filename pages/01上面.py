import streamlit as st
from PIL import Image
import pandas as pd

def drawline():
    data = pd.read_csv('up/whitepixels.csv')
    st.line_chart(data)

st.subheader('上面的俯视图')

# 播放视频
uploaded_file2 = st.file_uploader('选择上面视频')  # return type: BytesIO
if uploaded_file2 is not None:
    estimate = uploaded_file2.read()
    st.video(estimate)

if st.sidebar.button('提取关键帧'):

    # 计算白色像素点提取关键帧
    drawline()

    # 关键帧
    image = Image.open('up/input.jpg')
    st.image(image, caption='关键帧')

    # 关键帧二值化
    image_close = Image.open('up/img_close1.jpg')
    st.image(image_close, caption='关键帧二值化')

    # 关键帧二值化抠图
    image_kotuclose = Image.open('up/image_filtered.jpg')
    st.image(image_kotuclose, caption='关键帧二值化抠图')

    # 关键帧抠图
    image_kotu = Image.open('up/kotu.jpg')
    st.image(image_kotu, caption='关键帧抠图')




