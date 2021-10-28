import streamlit as st
from hydralit import HydraHeadApp

class PuzzleEasyApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
     def run(self):
        st.text("PuzzleEasyApp")
