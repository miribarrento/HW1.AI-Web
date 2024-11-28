import streamlit as st
from borrador_v2 import CountryGuesser

page = st.sidebar.selectbox("Please select a page", ["Developer Data", "Start Game"])

def display_developer_info():
    st.title("Developer Information")
    
    # Course and team members information
    st.header("AI and the Web - Homework 1: GuessGame")
    st.write("Professor: Tobias Thelen")
    st.write("Team Members:")
    st.write("- Raphael")
    st.write("- Mohit")
    st.write("- Martin")
    
    # Project Description
    st.subheader("Project Description")
    st.write("In this project, we are developing a country guessing game.")

if __name__ == "__main__":
    if page == "Developer Data":
        display_developer_info()  # Muestra la información de desarrolladores
    elif page == "Start Game":
        game = CountryGuesser()  # Inicia el juego


