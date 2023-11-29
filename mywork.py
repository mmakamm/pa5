import streamlit as st 
import pandas as pd
st.header("รร")
st.write("ไอเดียการเขียนแคปชั่นประกอบโพส โดยใช้ GPT-3 ของ OpenAI")
user_input = st.sidebar.text_input("Please add your OpenAI API key to continue", "you can get it from https://beta.openai.com/account/api-keys")    