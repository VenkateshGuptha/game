import streamlit as st
from hydralit import HydraHeadApp
from streamlit_player import st_player

class TutorialApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
         col1, col2 = st.columns(2)
         col1.text("Video");
         st_player("https://youtu.be/CmSKVW1v0xM")
