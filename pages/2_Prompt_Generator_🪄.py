import streamlit as st
from models.prompt_generator import prompt_gen
st.set_page_config(
    page_title="Prompt",
    page_icon="🧊",
    initial_sidebar_state="expanded",
)

def app():
    with st.sidebar:
        st.title('Prompt Generator🪄')
        if st.button('Clear Prompt'):
            st.session_state.clear()
    if prompt:=st.chat_input('Specify a task⚔️'):
        with st.spinner('Generating Prompt🪄'):
            with st.expander('Writing Prompt✏️'):
                response=st.write_stream(prompt_gen(prompt))
        
            st.code(response)
        
with open('Login.txt') as f:
    if f.read()=='True':
        app()
    else:
        st.write('Please Login!')

