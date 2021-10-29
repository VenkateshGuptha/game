import streamlit as st
from hydralit import HydraHeadApp
from typing import Dict
from pymongo import MongoClient

class LoginApp(HydraHeadApp):
     def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

     def run(self):
         col1, col2, col3 = st.columns(3)
         col2.title(self.title)
         login_form = col2.form(key="login_form")

         form_state = {}
         form_state['username'] = login_form.text_input('Username')
         form_state['submitted'] = login_form.form_submit_button('Login')
        
         if form_state['submitted']:
            self.Login(form_state, col2)

     def Login(self, form_data, msg_container) -> None:
        with st.spinner("Logging in...."):
            username = form_data['username'].lower()
            self.ValidateUserName(username)

     def ValidateUserName(self, username):
         client = MongoClient(st.secrets["url"])
         db = client.Game
         my_collections = db.Users
         rows = my_collections.find({"username": username}).sort('username')
         user = list(rows)
         if len(user) > 0:
            #user = list(rows)[0]
            self.LoginSuccess(user[0]['_id'])
         else:
            #self.ProfileSetup(username)
            self.CreateNewUser(username)
     
     def CreateNewUser(self, username):
         client = MongoClient(st.secrets["url"])
         db = client.Game
         my_collections = db.Users
         user = {'username':username}
         userRecord = my_collections.insert_one(user)
         self.LoginSuccess(userRecord.inserted_id)

     def ProfileSetup(self, username):
         login_form = st.form(key="profile_setup")

         form_state = {}
         form_state['firstname'] = login_form.text_input('First Name')
         form_state['lastname'] = login_form.text_input('Last Name')
         submit = login_form.form_submit_button('Submit')
        
         if submit:
            firstname = form_state['firstname']
            lastname = form_state['lastname']
            client = MongoClient(st.secrets["url"])
            db = client.Game
            my_collections = db.Users
            user = {'username':username, 'firstname':firstname, 'lastname':lastname}
            userRecord = my_collections.insert_one(user)
            #self.LoginSuccess(userRecord.inserted_id)

     def LoginSuccess(self, userid):
        #access control uses an int value to allow for levels of permission that can be set for each user, this can then be checked within each app seperately.
        self.set_access(1, 'username')
        self.session_state.UserID = userid
        #self.session_state.FirstName = firstname
        #self.session_state.LastName = lastname

        #Do the kick to the home page
        self.do_redirect()
           
        msg_container.error(f"Login unsuccessful, please check your username and password and try again.")
