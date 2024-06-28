import streamlit as st
from streamlit import session_state as sess
from models.claude import Chat

if 'model' not in sess:
    sess.model=Chat()
if 'chat_history' not in sess:
    sess.chat_history={'role':[],'type':[],'content':[]}


def display_chat():
    for content in sess.model.get_history():
        with st.chat_message(content['role']):
            st.write(content['content'])

def sidebar():
    with st.sidebar:
        st.title("God's Eye")
        if st.button('Clear history'):
            sess.model.clear_history()
def on_chat():
    display_chat()

def chat_ui():
    
    if prompt:=st.chat_input('Start',key='prompt',on_submit=on_chat):
        with st.chat_message('user'):
            st.write(prompt)
        with st.chat_message('assistant'):
            st.write_stream(sess.model.stream_chat(prompt))

sidebar()
chat_ui()



    

