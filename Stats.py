import streamlit as st
import pandas as pd

class Statisc:
    def __init__(self):
        st.title("Your Statistics! 📊")
        st.subheader("Detailed Statistics")
        st.write("Average Guesses needed")
        self.set_up_stats()
        self.display_statistics()

    
    def set_up_stats(self):

        default_values = {

            "wrong_guesses": 0,
            "number_of_guesses": [],
            "all_easy": 0, "guesses_easy": 0,
            "all_mid": 0, "guesses_mid": 0,
            "all_hard": 0, "guesses_hard": 0,
            "level": 0, "total_guesses": 0,
            "right_guesses": 0, "score": 0,
            "highscore": 0, "gewinner": "",
            "average_score": 0, "total_score": 0,
        }

        for key, value in default_values.items():
            if key not in st.session_state:
                st.session_state[key] = value
        
        # Inicializar el estado de las estadísticas
        if "average_score" not in st.session_state:
            st.session_state.average_score = 0
        if "total_guesses" not in st.session_state:
            st.session_state.total_guesses = 0
        if "right_guesses" not in st.session_state:
            st.session_state.right_guesses = 0
        if "gewinner" not in st.session_state:
            st.session_state.gewinner = ""
        if "highscore" not in st.session_state:
            st.session_state.highscore = 0
        if "all_easy" not in st.session_state:
            st.session_state.all_easy = 0
        if "guesses_easy" not in st.session_state:
            st.session_state.guesses_easy = 0
        if "all_mid" not in st.session_state:
            st.session_state.all_mid = 0
        if "guesses_mid" not in st.session_state:
            st.session_state.guesses_mid = 0
        if "all_hard" not in st.session_state:
            st.session_state.all_hard = 0
        if "guesses_hard" not in st.session_state:
            st.session_state.guesses_hard = 0
       
    def display_stats_cols(self):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Total Guesses", value=f"{st.session_state.total_guesses}")
        with col2:
            st.metric(label="Correct Guesses", value=f"{st.session_state.right_guesses}")
        with col3:
            st.metric(label="Average Guesses per Game", value=f"{average_score:.1f}")
        with col4:
            st.metric(label="Average Score", value=f"{st.session_state.average_score:.0f}")

    def calculate_average_guesses(self):
        try:
            return st.session_state.total_guesses / st.session_state.right_guesses
        except ZeroDivisionError:
            return st.session_state.total_guesses

    def calculate_average_easy(self):
        try:
            return st.session_state.all_easy / st.session_state.guesses_easy
        except ZeroDivisionError:
            return st.session_state.guesses_easy

    def calculate_average_mid(self):
        try:
            return st.session_state.guesses_mid / st.session_state.all_mid
        except ZeroDivisionError:
            return st.session_state.guesses_mid

    def calculate_average_hard(self):
        try:
            return st.session_state.guesses_hard / st.session_state.all_hard
        except ZeroDivisionError:
            return st.session_state.guesses_hard

    def display_statistics(self):
        # Calculamos los promedios
        average_guesses = self.calculate_average_guesses()
        average_easy = self.calculate_average_easy()
        average_mid = self.calculate_average_mid()
        average_hard = self.calculate_average_hard()

       


            
