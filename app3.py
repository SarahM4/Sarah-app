import streamlit as st
import random

st.title("Omikuji (おみくじ)")

omikuji_list = ["大吉", "吉", "中吉", "小吉", "末吉", "凶"]

button = st.button("Draw Omikuji")

if button:
    st.write("Result: " + random.choice(omikuji_list))
