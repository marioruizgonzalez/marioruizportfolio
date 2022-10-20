import streamlit as st
from multiapp import MultiApp
from streamlit_option_menu import option_menu
from apps import home, data, model


with st.sidebar:
    selected = option_menu("Mario Ruiz Porfolio", ["Machine Learning Projects", 'Data Mining PL/SQL', 'Resume / CV'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    selected
        

if selected == "Machine Learning Projects":
    st.title(f"You have selected {selected}")
    app = MultiApp()
    app.add_app("Projects Home", home.app)
    app.add_app("Projects Data", data.app)
    app.add_app("Projects Model", model.app)
    app.run()
if selected == "Data Mining PL/SQL":
    st.title(f"You have selected {selected}")
    app = MultiApp()
    app.add_app("PL Home", home.app)
    app.add_app("PL Data", data.app)
    app.add_app("PL Model", model.app)
    app.run()
if selected == "Resume / CV":
    st.title(f"You have selected {selected}")
    app = MultiApp()
    app.add_app("Resume Home", home.app)
    app.add_app("Resume Data", data.app)
    app.add_app("Resume Model", model.app)
    app.run()

app = MultiApp()


st.markdown("""
Select one option menu below.
""")


