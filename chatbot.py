import openai
import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="openai",
    layout='wide',
    initial_sidebar_state='auto',
)

st.header("Inroduction Generator for blog post")
st.write("ไอเดียการเขียนบทนำสำหรับบทความ")
st.sidebar.header("Inroduction Generator")
st.sidebar.text_input("Please add your OpenAI API key to continue", key='openai_apikey')

if st.session_state.openai_apikey != "":
    st.success('OpenAI API key provided!') #condition detect the invalid api_key
    st.text_input("ต้องการเขียนบทนำเรื่องกับอะไร", key = "chatbot_input")


    openai.api_key = st.session_state.openai_apikey
    prompt = f"Write 5 introductions for a blog post about {st.session_state.chatbot_input} and reason behind each introdution"
    def call_openai_api():
        try:
            response = openai.Completion.create(
                engine ="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=3000
            )
            return response
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded. Waiting before making the next request. Error: {e}")
            time.sleep(60)  # Wait for a minute
            return call_openai_api()

    response = call_openai_api()
    st.text_area("Response:", response.choices[0].text.strip())
    df = pd.DataFrame(response.choices[0].text.strip().split("\n"), columns=['caption'])
    df = df.dropna(axis=0)
    st.write(df)

else:
    st.warning('Please enter your OpenAI API key!')
