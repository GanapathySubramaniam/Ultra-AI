from models.openai import ChatGPT, tts2, transcribe_audio
import streamlit as st
from streamlit import session_state as sess
from streamlit_mic_recorder import mic_recorder
import asyncio
st.set_page_config(
    page_title="Voice Chat",
    page_icon="🧊",
    initial_sidebar_state="expanded",
)

with open('Login.txt') as f:
    if f.read()=='True':

        st.title('Voice Chat')


        if 'model' not in sess:
            sess['model'] = ChatGPT()

        async def process_audio(audio_bytes):
            # Use asyncio.to_thread for blocking operations
            text = await asyncio.to_thread(transcribe_audio, audio_bytes)
            
            response_stream = sess.model.stream_chat(text)
            full_response = ""
            
            for chunk in response_stream:
                full_response += chunk
                # Use st.empty() for real-time updates
            
            
            # Use asyncio.to_thread for TTS
            audio = await asyncio.to_thread(tts2, full_response)
            with st.sidebar:
                with st.expander('🔊'):
                    st.audio(audio, format="audio/mp3", start_time=0,autoplay=True)

        audio = mic_recorder(
            start_prompt="Start recording",
            stop_prompt="Stop recording",
            just_once=False,
            use_container_width=True,
            format="webm",
            callback=None,
            args=(),
            kwargs={},  
            key=None
        )

        if audio:
            with st.spinner('Processing...'):
                asyncio.run(process_audio(audio['bytes']))
    else:
        st.write('Please Login')