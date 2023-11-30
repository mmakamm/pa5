import openai
import streamlit as st
import pandas as pd

st.header("Caption Generator")
st.sidebar.header("Caption Generator")
openai_api_key = st.sidebar.text_input("Please add your OpenAI API key to continue", "")

if openai_api_key:
    st.sidebar.success('OpenAI API key provided!', icon='✅')
else:
    st.sidebar.warning('Please enter your OpenAI API key!', icon='⚠️')