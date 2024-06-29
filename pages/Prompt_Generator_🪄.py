import streamlit as st
from models.prompt_generator import prompt_gen
def app():
    with st.sidebar:
        st.title('Prompt Generator🪄')
    if prompt:=st.chat_input('Specify a task⚔️'):
        st.write_stream(prompt_gen(prompt))


app()

