import streamlit as st
import pandas as pd
from collections import Counter

def display_statistics():
    # Título principal
    st.title("Your Statistics! 📊")

    # Crear pestañas para cada juego
    tab1, tab2 = st.tabs(["🌎 Country Guesser", "🎲 Number Guesser"])

    # Inicializar variables en st.session_state si no existen
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

    # Calcular promedios con manejo de errores
    try:
        st.session_state.average_guesses = st.session_state.total_guesses / st.session_state.right_guesses
    except:
        st.session_state.average_guesses = st.session_state.total_guesses

    try:
        st.session_state.average_easy = st.session_state.all_easy / st.session_state.guesses_easy
    except:
        st.session_state.average_easy = st.session_state.guesses_easy

    try:
        st.session_state.average_mid = st.session_state.guesses_mid / st.session_state.all_mid
    except:
        st.session_state.average_mid = st.session_state.guesses_mid

    try:
        st.session_state.average_hard = st.session_state.guesses_hard / st.session_state.all_hard
    except:
        st.session_state.average_hard = st.session_state.guesses_hard

    # Estadísticas para Country Guesser
    with tab1:
        st.header("🌎 Country Guesser Statistics")
        col11, col22, col33 = st.columns(3)
        with col22:
            st.markdown("---")
            st.markdown(
                f"### <div style='text-align: center;'> 🏆 Highscore: {st.session_state.highscore:.0f} *by {st.session_state.gewinner}</div>*",
                unsafe_allow_html=True)
            st.markdown("---")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Total Guesses", value=f"{st.session_state.total_guesses}")
        with col2:
            st.metric(label="Correct Guesses", value=f"{st.session_state.right_guesses}")
        with col3:
            st.metric(label="Average Guesses per Game", value=f"{st.session_state.average_guesses:.1f}")
        with col4:
            st.metric(label="Average Score", value=f"{st.session_state.average_score:.0f}")

        # Gráfico de categorías
        st.subheader("Detailed Statistics")
        st.write("Average Guesses needed")
        categories = ["Easy", "Medium", "Hard"]
        values = [st.session_state.average_easy, st.session_state.average_mid, st.session_state.average_hard]
        data = pd.DataFrame({"Category": pd.Categorical(categories, categories=categories, ordered=True), "Value": values})
        st.bar_chart(data.set_index("Category"))

        st.markdown("---")
        st.write("How we estimate your Guess:")

    # Estadísticas para Number Guesser
    if "guesses" not in st.session_state:
        st.session_state.guesses = []
   
