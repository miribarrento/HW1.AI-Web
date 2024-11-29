import streamlit as st
from borrador_v2 import CountryGuesser
from displayinfodevs_v2 import display_developer_info
from Stats_Rapha import display_statistics

page = st.sidebar.selectbox("Please select a page", ["Developer Data", "Start Game", "Stats"])

if __name__ == "__main__":
    if page == "Developer Data":
        display = display_developer_info()  # Muestra la información de desarrolladores
    elif page == "Start Game":
        game = CountryGuesser()  # Inicia el juego
    elif page == "Stats":
        stat = display_statistics()
        



