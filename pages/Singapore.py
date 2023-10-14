import streamlit as st
from PIL import Image

st.title('Singapore シンガポール')
st.text('')  # 空行
st.text('')  # 空行
# マーライオン画像
image = Image.open('./Image/Singapore1.jpg')
st.image(image, width=500)
st.subheader('　マーライオン')
st.subheader('')  # 空行
# マリーナベイサンズ１画像
image = Image.open('./Image/Singapore3.jpg')
st.image(image, width=500)
st.subheader('　マリーナベイサンズ１')
st.subheader('')  # 空行
# マリーナベイサンズ２画像
image = Image.open('./Image/Singapore4.jpg')
st.image(image, width=500)
st.subheader('　マリーナベイサンズ２')
st.subheader('')  # 空行
# マリーナベイサンズ3画像
image = Image.open('./Image/Singapore5.jpg')
st.image(image, width=500)
st.subheader('　マリーナベイサンズ３')
st.subheader('')  # 空行
# ガーデンズバイザベイ画像
image = Image.open('./Image/Singapore6.jpg')
st.image(image, width=500)
st.subheader('　ガーデンズバイザベイ')
st.subheader('')  # 空行
# ガーデンズバイザベイ画像
image = Image.open('./Image/Singapore7.jpg')
st.image(image, width=500)
st.subheader('　ラッフルズホテル')
st.subheader('')  # 空行
# サルタンモスク画像
image = Image.open('./Image/Singapore8.jpg')
st.image(image, width=500)
st.subheader('　サルタンモスク')
st.subheader('')  # 空行
# セントーサ島画像
image = Image.open('./Image/Singapore9.jpg')
st.image(image, width=500)
st.subheader('　セントーサ島')
st.subheader('')  # 空行
# チャンギ国際空港・Jewel1画像
image = Image.open('./Image/Singapore10.jpg')
st.image(image, width=500)
st.subheader('　チャンギ国際空港・Jewel１')
st.subheader('')  # 空行
# チャンギ国際空港・Jewel2画像
image = Image.open('./Image/Singapore11.jpg')
st.image(image, width=500)
st.subheader('　チャンギ国際空港・Jewel２')
