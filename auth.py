import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader


def login():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )
    authenticator.login()
    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
        return True
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
        return False