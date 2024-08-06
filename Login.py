import streamlit as st
from streamlit import session_state as sess

with open('Login.txt','w') as f:
        f.write('False')

st.set_page_config(
    page_title="Ultra AI",
    page_icon="🧊",
    initial_sidebar_state="expanded",
)

with open('pwd.txt') as f:
     pwd=f.read()

st.header('Login 🗝️')
if st.text_input('Enter Password to Login!',type='password')==pwd:
    with open('Login.txt','w') as f:
        f.write('True')
    st.success('Logged In!')
else:
     st.error('Invalid Password')


