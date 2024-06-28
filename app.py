import streamlit as st
from streamlit import session_state as sess
from models.claude import Chat

if 'model' not in sess:
    sess.model=Chat()
if 'chat_history' not in sess:
    sess.chat_history={'role':[],'type':[],'content':[]}


def display_chat():
    ...

def sidebar():
    with st.sidebar:
        st.title("God's Eye")
def chat_ui():
   
    with st.chat_message('user'):
        st.write(prompt)

    if prompt:=st.chat_input('Start'):
         display_chat()
        with st.chat_input('assistant'):
            st.write_stream(sess.model.create_chat(prompt))



    

