import streamlit as st 
from streamlit import session_state as sess
from models.openai import image_gen_model
from datetime import datetime

st.set_page_config(
    page_title="Image",
    page_icon="🧊",
    initial_sidebar_state="expanded",
)


if 'recent_image' not in sess:
    sess.recent_image=None

if 'image_model' not in sess:
    sess['image_model']=image_gen_model()
for img in sess.image_model.images:
    with st.sidebar:
        st.image(img)
def display_image_chat():
    for message in sess.image_model.history:
        if (message['role']=='user'):
            with st.chat_message('user'):
                    st.markdown(message["content"])
        else:
            if (message['type']=='image'):
                with st.chat_message('assitant'):
                    sess.recent_image=message['content']
                    st.image(message['content'])

def display_image_sidebar():
    with st.sidebar:
        image_sizes=['1024x1024', '1024x1792','1792x1024']
        image_qualities=['standard','hd'] 
        sess.image_model.size=st.selectbox('Image Size',image_sizes)
        sess.image_model.quality=st.selectbox('Image Quality',image_qualities)
        sess.image_model.style=st.select_slider('Style',['natural','vivid'] )

        c1,c2=st.columns(2)
        with c1:
            if st.button('Clear Chat'):
                sess.image_model.clear_history()
        with c2:
            if sess.recent_image:
                st.download_button(
                        label="Download Generated image",
                        data=sess.recent_image,
                        file_name=f"Generated_image_{datetime.now().timestamp()}.png",
                        mime="image/png"
                    )
  
def image_chat_ui():  
    display_image_chat()
    if prompt := st.chat_input("Creativity is imagination in Reality! Let's create!🖌️"):
        sess.image_model.image_chat(prompt)
        display_image_chat()

def app():
    display_image_sidebar()
    image_chat_ui()

with open('Login.txt') as f:
    if f.read()=='True':
        app()
    else:
        st.write('Please Login!')
