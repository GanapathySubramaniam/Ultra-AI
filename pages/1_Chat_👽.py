'''
!!!!! Clear button needs to be clicked twice 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
import streamlit as st
from streamlit import session_state as sess
from auth import login
from models.claude import Chat
from models.openai import tts
from glob import glob

if 'model' not in sess:
    sess.model=Chat()

def check_add_states(key,val):
    if key not in sess:
        sess[key]=val


check_add_states('chat_history',{'role':[],'type':[],'content':[]})
check_add_states('temp',sess.model.temperature)
check_add_states('max_tok',sess.model.max_tokens)
check_add_states('sys_inst',sess.model.system_instructions)
buttons=['settings','camera_inp','files_inp','display']


for btn in buttons:
    check_add_states(btn,False)

def refresh_params():
    sess.model.system_instructions=sess.sys_inst
    sess.model.temperature=sess.temp
    sess.model.max_tokens=sess.max_tok
    sess.settings=True

if sess.display:
    for content in sess.model.get_history():
        with st.chat_message(content['role']):
            st.write(content['content'])

def sidebar():
    with st.sidebar:
        st.title("Chat 👽")
        with st.expander('🛠️'):
            c1,c2,c3=st.columns(3,gap='small',vertical_alignment='center')
            with c1:
                settings=st.button('⚙️')
                
            with c2:
                cam=st.button('📷')
                        
            with c3:
                files= st.button('📁')
        c4,c5,c6,c7,c8=st.columns(5)            
        with c7:
            if st.button('🗑️',key='clear'):
                sess.display=False
                sess.model.clear_history()
        with c8:
            audio= st.button('🔊')
                
        placeholder=st.expander('👑')
        if audio:
            with placeholder:
                st.audio(tts(sess.model.get_history()[-1]['content']),autoplay=True)
        if settings | sess.settings:
            with placeholder:
                st.text_area('System Instructions',key='sys_inst',value=sess.sys_inst,on_change=refresh_params)
                st.slider('Temperature',key='temp',min_value=0.1,value=sess.temp,max_value=1.0,step=0.1,on_change=refresh_params)
                st.select_slider('Max Tokens',[100,500,1000,1500],value=sess.max_tok,key='max_tok',on_change=refresh_params)
        if cam | sess.camera_inp:
            with placeholder:
                st.camera_input('📷',disabled=False,key='camera')
        if files | sess.files_inp:
            with placeholder:
                st.file_uploader('🖇️',accept_multiple_files=True,label_visibility='hidden',key='files')
             
def chat_ui():
    if prompt:=st.chat_input('Start✨',key='prompt'):
        sess.display=True
        with st.chat_message('user'):
            st.write(prompt)
        with st.chat_message('assistant'):
            st.write_stream(sess.model.stream_chat(prompt))


def app():
    sidebar()
    chat_ui()

if st.session_state["authentication_status"]:
    app()
else:
    st.write('Login to use!')
    

