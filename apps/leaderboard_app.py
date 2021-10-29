import streamlit as st
from hydralit import HydraHeadApp
from pymongo import MongoClient
import numpy as np
import pandas as pd
from st_aggrid import AgGrid

class LeaderBoardApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.UserNames = {}

     def run(self):
        self.LoadData()

        data = []
        for row in self.currentPuzzleData:
            data.append((self.GetUserName(str(row['userid'])), row['puzzlenumber'], row['totaldistance'], row['infilldistance'], row['transitdistance']))
        
        data = pd.DataFrame(np.array(data), columns=['Username', 'Puzzle #', 'Total Distance', 'InFile distance', 'Transit Distance'])
        data = AgGrid(data)

     def LoadData(self):
        client = MongoClient(st.secrets["url"])
        db = client.Game
        my_collections = db.PuzzleResults
        self.currentPuzzleData = my_collections.find().sort('totaldistance')
        self.Users = list(self.GetAllUsers())

     def GetAllUsers(self):
        client = MongoClient(st.secrets["url"])
        db = client.Game
        return db.Users.find()

     def GetUserName(self, userid):
        for user in self.Users:
            if str(user['_id']) == userid:
                return user['username']

        return ''