import streamlit as st 
from streamlit import session_state as sess
from models.openai import image_gen_model

if 'image_model' not in sess:
    sess['image_model']=image_gen_model()

def display_image_chat():
    for message in sess.image_model.history:
        with st.chat_message(message["role"]):
            if message['type']=='text':
                st.markdown(message["content"])
            else:
                 st.image(message['content'])

def display_image_sidebar():
    with st.sidebar:
        image_sizes=['1024x1024', '1024x1792','1792x1024']
        image_qualities=['standard','hd'] 
        sess.image_model.size=st.selectbox('Image Size',image_sizes)
        sess.image_model.quality=st.selectbox('Image Quality',image_qualities)

        c1,c2=st.columns(2)
        with c1:
            if st.button('Clear Chat'):
                sess.image_model.clear_history()
  
def image_chat_ui():  
    display_image_chat()
    if prompt := st.chat_input("Creativity is imagination in Reality! Let's create!"):
        sess.image_model.image_chat(prompt)
        display_image_chat()

def image_chat():
    display_image_sidebar()
    image_chat_ui()

image_chat()