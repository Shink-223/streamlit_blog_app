import streamlit as st
from PIL import Image

st.title('Malaysia マレーシア')
st.text('')  # 空行
st.text('')  # 空行
# タブ
tab1,tab2 = st.tabs(['Kuala Lumpur','Penang'])
with tab1:
    st.header('Kuala Lumpur クアラルンプール')
    st.subheader('')  # 空行
    # KLの夜景１画像
    image = Image.open('./Image/KL1.jpg')
    st.image(image, width=500)
    st.subheader('　KLの夜景１')
    st.subheader('')  # 空行
    # KLの夜景２画像
    image = Image.open('./Image/KL2.jpg')
    st.image(image, width=500)
    st.subheader('　KLの夜景２')
    st.subheader('')  # 空行
    # ペエトロナスツインタワー画像
    image = Image.open('./Image/KL3.jpg')
    st.image(image, width=500)
    st.subheader('　ペトロナスツインタワー')
    st.subheader('')  # 空行
    # バトゥ洞窟画像
    image = Image.open('./Image/KL4.jpg')
    st.image(image, width=500)
    st.subheader('　バトゥ洞窟')
    st.subheader('')  # 空行

with tab2:
    st.header('Penang ペナン')
    st.text('')  # 空行
    st.text('')  # 空行
    # バトゥ・フェリンギ画像
    image = Image.open('./Image/Penang1.jpg')
    st.image(image, width=500)
    st.subheader('　バトゥ・フェリンギビーチ')
    st.subheader('')  # 空行
    # バトゥ・フェリンギ夕日画像
    image = Image.open('./Image/Penang2.jpg')
    st.image(image, width=500)
    st.subheader('　バトゥ・フェリンギビーチの夕日')
    st.subheader('')  # 空行
    # マレーシア国旗とペナン州旗画像
    image = Image.open('./Image/Penang3.jpg')
    st.image(image, width=500)
    st.subheader('　マレーシア国旗とペナン州旗')
    st.subheader('')  # 空行
    # ジョージタウン画像
    image = Image.open('./Image/Penang4.jpg')
    st.image(image, width=500)
    st.subheader('　ジョージタウン')
    st.subheader('')  # 空行
    # xii chan画像
    image = Image.open('./Image/Penang5.jpg')
    st.image(image, width=500)
    st.subheader('　xii chan')
    st.subheader('')  # 空行
    # Chew Jetty画像
    image = Image.open('./Image/Penang6.jpg')
    st.image(image, width=500)
    st.subheader('　Chew Jetty')
    st.subheader('')  # 空行
