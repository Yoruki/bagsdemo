import cv2
import streamlit as st
from PIL import Image
import pytesseract

st.subheader("# 文字识别 ")
st.sidebar.markdown("# 文字识别 ")

image = Image.open('pics/left/thresh131.jpg')
image_cut = Image.open('pics/number/code.jpg')
st.image(image, caption='文字识别')
st.image(image_cut,caption='编号剪切')

# 二值化
a = 90
img = cv2.imread('pics/number/code.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY)
st.image(thresh,caption='图片二值化')
# 文字识别
# OCR()
# text = pytesseract.image_to_string(thresh, lang='eng')
# st.write(text)

