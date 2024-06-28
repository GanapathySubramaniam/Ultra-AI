import streamlit as st
from streamlit import session_state as sess
from models.claude import Chat

if 'model' not in sess:
    sess.model=Chat()
if 'chat_history' not in sess:
    sess.chat_history={'role':[],'type':[],'content':[]}


def display_chat():
    

