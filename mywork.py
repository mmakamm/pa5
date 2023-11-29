import streamlit as st 
import pandas as pd
st.header("Caption Generator")
st.write("ไอเดียการเขียนแคปชั่นประกอบโพส โดยใช้ GPT-3 ของ OpenAI")
st.set_page_config(page_title="💬Caption Generator")
                   
openai_api_key = st.sidebar.text_input("Please add your OpenAI API key to continue", "")
if openai_api_key:
    st.sidebar.success('OpenAI API key provided!', icon='✅')
else:
    st.sidebar.warning('Please enter your OpenAI API key!', icon='⚠️')

chatbot_input = st.text_input("ต้องการเขียนแคปชั่นเกี่ยวกับอะไร")   