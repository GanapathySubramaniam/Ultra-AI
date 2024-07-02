import streamlit as st
from auth import login
from models.prompt_generator import prompt_gen
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
        
if st.session_state["authentication_status"]:
    app()
else:
    st.write('Login to use!')
