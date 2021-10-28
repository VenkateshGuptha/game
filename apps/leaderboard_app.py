import streamlit as st
from hydralit import HydraHeadApp

class LeaderBoardApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
        st.text("LeaderBoard")
