import streamlit as st
from streamlit import session_state as sess
from auth import login
from models.claude import Chat
from models.openai import tts
from base64 import b64encode
from glob import glob

if 'model' not in sess:
    sess.model=Chat()

def check_add_states(key,val):
    if key not in sess:
        sess[key]=val

def callback(btn):
    sess[btn]=True

check_add_states('images',[])
check_add_states('temp',sess.model.temperature)
check_add_states('max_tok',sess.model.max_tokens)
check_add_states('sys_inst',sess.model.system_instructions)
check_add_states('prompt',[])
buttons=['⚙️','📷','🔊','settings','audio','camera_inp','files','display']
for btn in buttons:
    check_add_states(btn,False)

def process_image(img_file):
    img_content={"type":"image"}
    img_content['source']={"type": "base64","media_type":img_file.type ,"data":b64encode(img_file.read()).decode("utf-8")}
    sess.prompt.append(img_content)
    return img_content

def check_for_file_uploads():
    if sess.files_upload:
        for file in sess.files_upload:
            if file.type.startswith('image'):
                process_image(file)
        return True
    return False

def get_image():
    img=sess.camera
    if img:
        img_data=b64encode(img.getvalue()).decode("utf-8")
        img_content={"type":"image"}
        img_content['source']={"type": "base64","media_type":img.type ,"data":img_data}
        sess.prompt.append(img_content)

def refresh_params():
    sess.model.system_instructions=sess.sys_inst
    sess.model.temperature=sess.temp
    sess.model.max_tokens=sess.max_tok
    sess.settings=True

def clear_contents():
    sess.display=False
    sess.model.clear_history()
    sess.prompt=[]
    sess.files_upload=[]
    sess['📁']=False
    sess.files=False
    sess['📷']=False
    sess.camera_inp=False
    sess.model=Chat()
    sess.model.system_instructions=sess.model.system_instructions
    sess.model.temperature=sess.model.temperature
    sess.model.max_tokens=sess.model.max_tokens

def copy():
      with st.sidebar:
        with st.expander('📋',):
                try:
                    st.code(sess.model.get_history()[-1]['content'][0]['text'])
                except Exception as e:
                    st.code("...")
if st.session_state["authentication_status"]:
    if sess.display:
        for contents in sess.model.get_history():
            role=contents['role']
            with st.chat_message(role):
                for content in contents.get('content'):
                    if content['type']=='text':
                        st.write(content["text"])



    with st.sidebar:
        st.title("Chat 👽")
        settings_placeholder=st.expander('⚙️')
        camera_placeholder=st.expander('📷')
        files_placeholder=st.expander('📁')
        audio_placeholder=st.expander('🔊')

        with st.expander('🛠️'):
            c1,c2,c3,c4,c5=st.columns(5,gap='small',vertical_alignment='center')
            with c1:
                if st.button('⚙️',on_click=callback,args=['settings']) | sess.settings:
                    sess.camera_inp=False
                    sess.files=False
                    with settings_placeholder:
                        st.text_area('System Instructions',key='sys_inst',value=sess.sys_inst,on_change=refresh_params)
                        st.slider('Temperature',key='temp',min_value=0.1,value=sess.temp,max_value=1.0,step=0.1,on_change=refresh_params)
                        st.select_slider('Max Tokens',[100,500,1000,1500],value=sess.max_tok,key='max_tok',on_change=refresh_params)
            with c2:
                if st.button('📷',on_click=callback,args=['camera_inp']) | sess.camera_inp:
                    sess.files=False
                    sess.settings=False
                    with camera_placeholder:
                        st.camera_input('📷',disabled=False,key='camera',on_change=get_image)
                        
            with c3:
                if st.button('📁',on_click=callback,args=['files']) | sess.files:
                    sess.settings=False
                    sess.camera_inp=False
                    with files_placeholder:
                        st.file_uploader('🖇️',accept_multiple_files=True,label_visibility='hidden',key='files_upload',on_change=check_for_file_uploads)
            with c4:
                st.button('🗑️',key='clear',on_click=clear_contents)
                    
            with c5:
                if st.button('🔊',on_click=callback,args=['audio']):
                    with audio_placeholder:
                        try:
                            st.audio(tts(sess.model.get_history()[-1]['content']),autoplay=True)
                        except Exception as e:
                            print(e)
      

    if prompt:=st.chat_input('Start✨',key='prompt_inp'):
        prompt={"type":"text","text":prompt}
        sess.prompt.append(prompt)
        sess.display=True
        sess.files=False
        sess['📁']=False
        with st.chat_message('user'):
            st.write(prompt['text'])
        with st.chat_message('assistant'):
            st.write_stream(sess.model.stream_chat(sess.prompt))
            sess.prompt=[]
            sess.files=False
        copy()






else:
    st.write('Login to use!')
    

