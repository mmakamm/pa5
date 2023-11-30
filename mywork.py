import openai
import streamlit as st

# Load OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Introduction
st.title("🧑‍💻 Data-Espresso 💬 Bot")
"""
สวัสดีครับ ผมคือ Data-barista Bot ☕️ . 
ยินดีที่ได้รู้จักนะครับ มีหลายอย่างที่ผมรู้ และผมตอบได้ อยากรู้อะไรถามมาได้เลยครับ แต่อย่าถามกวนนะ เดี๋ยวจะหาว่าไม่เตือน อิๆ 😀
"""

# Set the role of the chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [
    {"role": "system", "content": "You are a data analytics expert called Data-Barista, you love to use emojis. You are professional on data analytics and data science"}
    ]

# Parse user input to the chartGPT API
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)