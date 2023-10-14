import streamlit as st
from PIL import Image

# テキスト関連
st.title('異国の風景 旅の写真集')
st.text('') # 空行
st.subheader('海外旅行の写真ギャラリーにようこそ！')
st.text('ここでは私がこれまで旅をした場所で撮影された写真をご覧いただけます。')
st.text('') # 空行
st.text('') # 空行
st.text('私のnote')
note_url = "https://note.com/famous_koala398"
st.write(note_url)
# 画像
image = Image.open('./Image/Home画面用.jpg')
st.image(image, width=500)
