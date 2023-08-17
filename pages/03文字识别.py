import streamlit as st
from PIL import Image

st.subheader("# 文字识别 ")
st.sidebar.markdown("# 文字识别 ")

image = Image.open('number/thresh131.jpg')
image_cut = Image.open('number/code.jpg')
st.image(image, caption='文字识别')
st.image(image_cut,caption='编号剪切')

# 二值化
img = Image.open('number/valuecode.jpg')
st.image(img,caption='图片二值化')
# 文字识别
# OCR()
# text = pytesseract.image_to_string(thresh, lang='eng')
# st.write(text)

