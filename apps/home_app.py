import streamlit as st
from hydralit import HydraHeadApp

class HomeApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def _userName(self):
          return "Venkatesh"

     def run(self):
          st.title("Home App")
