import streamlit as st
import hydralit as hy
import apps

over_theme = {'txc_inactive': '#FFFFFF'}
app = hy.HydraApp(title='Navigation App', hide_streamlit_markers=False,use_navbar=True, navbar_sticky=False)

app.add_app("Home", app=apps.HomeApp(title='Home', is_home=True))
app.add_app("Tutorial", app=apps.TutorialApp(title='Tutorial'))
app.add_app("Puzzle - Easy", app=apps.PuzzleEasyApp(title='Puzzle - Easy'))
app.add_app("Puzzle - Easy - 2", app=apps.PuzzleMediumApp(title='Puzzle - Easy - 2'))
app.add_app("Puzzle - Medium", app=apps.PuzzleHardApp(title='Puzzle - Medium'))
app.add_app("Scores", app=apps.LeaderBoardApp(title='Leaderboard'))

app.add_app("Login", apps.LoginApp(title='Login'),is_login=True) 

complex_nav = {
    'Intro':['Home'],
    'Tutorial':['Tutorial'],
    'Play':['Puzzle - Easy', 'Puzzle - Easy - 2', 'Puzzle - Medium'],
    'Scores':['Scores']
}

#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run(complex_nav)
    
