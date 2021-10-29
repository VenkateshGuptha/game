import streamlit as st
from hydralit import HydraHeadApp
from pymongo import MongoClient
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

class LeaderBoardApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.UserNames = {}

     def run(self):
        self.LoadData()

        data = []
        for row in self.currentPuzzleData:
            data.append((self.GetUserName(str(row['userid'])), row['infilldistance'], row['totaldistance']))
        
        data = pd.DataFrame(np.array(data), columns=['Username', 'InFile distance', 'Total Distance'])
        gb = GridOptionsBuilder.from_dataframe(data)
        gb.configure_selection(selection_mode='single')
        go = gb.build()
        #st.dataframe(data)
        data = AgGrid(data, gridOptions=go, update_mode=GridUpdateMode.SELECTION_CHANGED)
        selecteddf = pd.DataFrame(data['selected_rows'])
        st.text(selecteddf)

     def LoadData(self):
        client = MongoClient(st.secrets["url"])
        db = client.Game
        my_collections = db.PuzzleResults
        self.currentPuzzleData = my_collections.find({"puzzlenumber": 2}).sort('totaldistance')
        self.Users = list(self.GetAllUsers())

     def GetAllUsers(self):
        client = MongoClient(st.secrets["url"])
        db = client.Game
        return db.Users.find()

     #@st.cache(persist=True, hash_funcs={st.delta_generator.DeltaGenerator: id, pymongo.write_concern.WriteConcern: id})
     def GetUserName(self, userid):
        for user in self.Users:
            if str(user['_id']) == userid:
                return user['username']

        return ''