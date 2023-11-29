import streamlit as st 
import pandas as pd
st.header("Hello World 👏")
st.write("This is my first app")
user_input = st.sidebar.text_input("Please add your OpenAI API key to continue", "you can get it from https://beta.openai.com/account/api-keys")    