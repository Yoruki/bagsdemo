# main_page.py内容
import streamlit as st

st.markdown("# 编织袋计量与识别演示")
st.subheader('基于streamlit实现的基于opencv的图像识别Demo')
st.sidebar.markdown("# 编织袋计量与识别演示")
st.text('编程人员：徐宙杰、韩蕾')
st.subheader('编程说明：')
st.text('（1）目的是为了后续的计量和文字识别作演示')
st.text('（2）分成顶上的摄像机视频处理、侧面摄像机视频处理以及文字设别摄像机视频处理三个部分')
st.text('（3）侧面负责计量编织袋的层数C，上面负责计量最上层的编织袋的数量S，总的报数就是5*（C-1）+S')
st.text('（4）文字识别是编制袋上打印的序列号')