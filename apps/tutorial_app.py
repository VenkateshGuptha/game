import streamlit as st
from hydralit import HydraHeadApp
from streamlit_player import st_player

class TutorialApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
         col1, col2, col3 = st.columns(3)
         #st_player("https://youtu.be/CmSKVW1v0xM")
         video_file = open('resources/Full Tutorial.mp4', 'rb')
         video_bytes = video_file.read()
         col2.video(video_bytes)
