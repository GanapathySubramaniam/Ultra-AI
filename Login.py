import streamlit as st
from auth import login
st.session_state["authentication_status"]=False
st.set_page_config(
    page_title="Ultra AI",
    page_icon="🧊",
    initial_sidebar_state="expanded",
)
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"]=''
st.title('Login 🗝️')

login()
