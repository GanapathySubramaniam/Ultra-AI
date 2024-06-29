import streamlit as st
from streamlit import session_state as sess
from models.claude import Chat
from glob import glob

if 'model' not in sess:
    sess.model=Chat()
if 'chat_history' not in sess:
    sess.chat_history={'role':[],'type':[],'content':[]}


def display_chat():
    for content in sess.model.get_history():
        with st.chat_message(content['role']):
            st.write(content['content'])



def sidebar():
    with st.sidebar:
        st.title("God's Eye")
        c4,c5,c6,c1,c2,c3=st.columns(6)
        camera_expander=st.expander('📷')
        file_expander=st.expander('📁')
        expander=st.expander('⚙️')
        with c6:
            if st.button('⚙️'):
                sess.model.system_instructions=expander.text_area('System Instructions')
                sess.model.temperature=expander.slider('Temperature',min_value=0.1,max_value=1.0,step=0.1,value=1.0)
                sess.model.max_tokens=expander.select_slider('Max Tokens',[100,500,1000],value=500)
            
        with c1:
            if st.button('📷'):
                    camera_expander.camera_input('📷',disabled=False,key='camera')
        with c2:
            if st.button('📁'):
                file_expander.file_uploader('🖇️',accept_multiple_files=True,label_visibility='hidden',key='files')
        with c3:
            if st.button('🗑️'):
                sess.model.clear_history()
      
        
def on_chat():
    display_chat()

def chat_ui():
    if prompt:=st.chat_input('Start✨',key='prompt',on_submit=on_chat):
        with st.chat_message('user'):
            st.write(prompt)
        with st.chat_message('assistant'):
            st.write_stream(sess.model.stream_chat(prompt))

def apply_styles():
    style_markdowns=[]
    for css_file_path in glob('styles/*.css'):
        with open(css_file_path) as css_file:
            style_markdowns.append(css_file.read())

    style_markdowns='\n'.join(style_markdowns)
    style_tag='<style>{markdown}</style'.format(markdown=style_markdowns)
    st.markdown(style_tag,unsafe_allow_html=True)


def app():
    apply_styles()
    sidebar()
    chat_ui()


app()
    

