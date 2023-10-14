import streamlit as st
from PIL import Image

st.title('Thailand タイ')
st.text('')  # 空行
st.text('')  # 空行
# タブ
tab1, tab2 = st.tabs(['Bangkok', 'Phuket'])
with tab1:
    st.header('Bangkok バンコク')
    st.subheader('')  # 空行
    # ワット・ポー画像
    image = Image.open('./Image/Bangkok1.jpg')
    st.image(image, width=500)
    st.subheader('　ワット・ポー')
    st.subheader('')  # 空行
    # ワット・アルン画像
    image = Image.open('./Image/Bangkok3.jpg')
    st.image(image, width=500)
    st.subheader('　ワット・アルン')
    st.caption('')  # 空行
    # 虹画像
    image = Image.open('./Image/Bangkok2.jpg')
    st.image(image, width=500)
    st.subheader('　スクンビット駅にて１')
    st.caption('')  # 空行
    # 虹画像
    image = Image.open('./Image/Bangkok4.jpg')
    st.image(image, width=500)
    st.subheader('　スクンビット駅にて２')
    st.caption('')  # 空行

with tab2:
    st.header('Phuket プーケット')
    st.subheader('')  # 空行
    # パトン夕日画像
    image = Image.open('./Image/Phuket1.jpg')
    st.image(image, width=500)
    st.subheader('　パトンビーチの夕日')
    st.caption('')  # 空行
    # パトン画像
    image = Image.open('./Image/Phuket2.jpg')
    st.image(image, width=500)
    st.subheader('　パトンビーチ')
    st.caption('')  # 空行
    # バングラ通り画像
    image = Image.open('./Image/Phuket3.jpg')
    st.image(image, width=500)
    st.subheader('　バングラ通り')
    st.caption('')  # 空行
    # エレファントキャンプ画像
    image = Image.open('./Image/Phuket4.jpg')
    st.image(image, width=500)
    st.subheader('　エレファントキャンプ')
    st.caption('')  # 空行
