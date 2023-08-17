import streamlit as st

st.subheader("# 总结 ")

upNumber = 5
st.text('上面编织袋包数：%d' % upNumber)

leftLayer = 9
st.text('左边编织袋层数：%d' % leftLayer)

bagNumber = upNumber+(leftLayer-1)*5
st.text('编织袋总包数：%d' % bagNumber)

ocr = 'AGISEI-H H3717AN J118'
st.text('文字识别结果：%s' % ocr)