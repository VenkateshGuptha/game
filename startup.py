import streamlit as st
import hydralit as hy
import apps

over_theme = {'txc_inactive': '#FFFFFF'}
app = hy.HydraApp(title='Navigation App', hide_streamlit_markers=False,use_navbar=True, navbar_sticky=False)

app.add_app("Home", app=apps.HomeApp(title='Home', is_home=True))
app.add_app("Puzzle - Easy", app=apps.PuzzleEasyApp(title='Puzzle - Easy'))
app.add_app("Puzzle - Medium", app=apps.PuzzleMediumApp(title='Puzzle - Medium'))
app.add_app("Puzzle - Hard", app=apps.PuzzleHardApp(title='Puzzle - Hard'))
app.add_app("Leaderboard", app=apps.LeaderBoardApp(title='Leaderboard'))

#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()
    
