import streamlit as st
from auth import login

st.set_page_config(
    page_title="Ultra AI",
    page_icon="🧊",
    initial_sidebar_state="expanded",
)

st.header('Login 🗝️')

login()
