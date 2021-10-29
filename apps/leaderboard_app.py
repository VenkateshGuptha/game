import streamlit as st
from hydralit import HydraHeadApp
from pymongo import MongoClient
import numpy as np

class LeaderBoardApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.UserNames = {}

     def run(self):
        st.text("LeaderBoard")
        self.LoadData()

        data = []
        for row in self.currentPuzzleData:
            data.append((self.GetUserName(str(row['userid'])), row['infilldistance'], row['totaldistance']))
        
        st.dataframe(np.array(data))

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
        '''user = db.Users.find_one({'_id':userid})
        if user is None:
            return ""

        return user['username']'''

     def GetUserName(self, userid):

        for user in self.Users:
            if str(user['_id']) == userid:
                return user['username']

        return ''