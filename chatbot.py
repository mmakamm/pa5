import openai
import streamlit as st
from streamlit.report_thread import get_report_ctx

class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


# Function to get or create the session state
def get_session_state():
    session = get_report_ctx().session
    if not hasattr(session, "_custom_session_state"):
        session._custom_session_state = SessionState()
    return session._custom_session_state

st.set_page_config(
    page_title="openai",
    layout='wide',
    initial_sidebar_state='auto',
)

# Initialize session state
session_state = get_session_state()

# Rest of your code remains unchanged
# ...

if session_state.openai_apikey != "":
    st.set_page_config(
    page_title="openai",
    layout='wide',
    initial_sidebar_state='auto',
)

# Initialize session state
if 'openai_apikey' not in st.session_state:
    st.session_state.openai_apikey = ""
if 'chatbot_input' not in st.session_state:
    st.session_state.chatbot_input = ""

st.header("Caption Generator")
st.write("ไอเดียการเขียนแคปชั่นประกอบโพส")
st.sidebar.header("Caption Generator")
st.sidebar.text_input("Please add your OpenAI API key to continue", key='openai_apikey')

if st.session_state.openai_apikey != "":
    st.success('OpenAI API key provided!')
    st.text_input("ต้องการเขียนแคปชั่นเกี่ยวกับอะไร", key="chatbot_input")

    openai.api_key = st.session_state.openai_apikey
    prompt = f"Write 5 introductions for a blog post about {st.session_state.chatbot_input} and reason why I should use them"

    response = None
    def call_openai_api():
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=3000
            )
            return response
        except Exception as e:
            st.error(f"Error occurred: {e}")

    session_state.sync()  # Sync session state before calling the API
    response = call_openai_api()
    if response:
        st.text_area("Response:", response.choices[0].text.strip())

else:
    st.warning('Please enter your OpenAI API key!', icon='⚠️')
