import streamlit as st
import random
from Data import countries_mid, countries_easy, countries_hard, country_all

class CountryGuesser:
    
    def __init__(self):
        self.setup_session_state()
        st.title("Welcome to CountryGuesser! 🌎")
        self.display_intro()
    
    def setup_session_state(self):
        # Initialize session state variables if not already defined
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
            "space_letters": [],
            "random_country_easy": random.choice(countries_easy),
            "random_country_mid": random.choice(countries_mid),
            "random_country_hard": random.choice(countries_hard),
            "hints": []  # Almacenará las pistas
        }
        for key, value in default_values.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def display_intro(self):
        st.write("Select a difficulty to start:")
        self.display_hint_buttons()  
        self.start_game()
    
    def display_hint_buttons(self):
        col1, col2, col3 = st.columns([0.6, 0.755, 1])
        with col1:
            if st.button("Easy 🧸"):
                self.set_game(1)
        with col2:
            if st.button("Medium ⚖️"):
                self.set_game(2)
        with col3:
            if st.button("Hard ⚔️"):
                self.set_game(3)

    def set_game(self, level):
        st.session_state.wrong_guesses = 0
        st.session_state.level = level
        self.reset_country(level)

    def reset_country(self, level):
        if level == 1:
            st.session_state.random_country_easy = random.choice(countries_easy)
        elif level == 2:
            st.session_state.random_country_mid = random.choice(countries_mid)
        elif level == 3:
            st.session_state.random_country_hard = random.choice(countries_hard)
        
        if level == 1:
            country = st.session_state.random_country_easy
        elif level == 2:
            country = st.session_state.random_country_mid
        elif level == 3:
            country = st.session_state.random_country_hard
        
        st.session_state.space_letters = ["_" if char != " " else " " for char in country['name']]
        st.session_state.hints = []  # Clear previous hints

    def start_game(self):
        if st.session_state.level:
            country = self.get_current_country()
            st.write(f"**To get you started, here's a hint:** ")
            st.write(f"{country['fact']}")
            st.text(f"Country 🗺️: {' '.join(st.session_state['space_letters'])}")
            self.handle_user_input(country)
    
    def get_current_country(self):
        if st.session_state.level == 1:
            return st.session_state.random_country_easy
        elif st.session_state.level == 2:
            return st.session_state.random_country_mid
        elif st.session_state.level == 3:
            return st.session_state.random_country_hard
    
    def handle_user_input(self, country):
        user_guess = st.chat_input("Enter your guess")
        if user_guess:
            self.check_guess(user_guess, country)

    def check_guess(self, guess, country):
        level = st.session_state.level
        if guess == country["name"]:
            self.game_won(level)
        else:
            st.error("Nope, that's not correct.")
            self.process_wrong_guess(country)

    def process_wrong_guess(self, country):
        st.session_state.wrong_guesses += 1
        st.session_state.score -= 3
        if st.session_state.wrong_guesses == 2:
            hint = f"Typical food: {country['food']}"
            st.session_state.hints.append(hint)
        elif st.session_state.wrong_guesses == 4:
            hint = f"Language: {country['language']}"
            st.session_state.hints.append(hint)
        elif st.session_state.wrong_guesses == 6:
            st.text(f"Warning Adventurer, this is your last chance!")
        if st.session_state.wrong_guesses == 7:
            self.game_lost()
        self.display_hints()

    def display_hints(self):
        # Aquí vamos a crear las columnas
        col1, col2 = st.columns([4, 1])
        with col2:
            st.subheader("Hints: 💡")
            for hint in st.session_state.hints:
                st.write(f"- {hint}")
        
    def game_won(self, level):
        country = self.get_current_country() 
        st.session_state.right_guesses += 1
        # Ajuste del puntaje basado en el nivel de dificultad
        if level == 1:
            st.session_state.score += 10
        elif level == 2:
            st.session_state.score += 15
        elif level == 3:
            st.session_state.score += 20
        st.write(f"Score 🏆: {st.session_state.score:}")
    
        # Mostrar el mensaje indicando que el jugador puede elegir un nuevo nivel
        st.success(f"Correct! The country was {country['name']}. Click on a level again to continue guessing or reset.")
        self.reset_country(level)
        self.update_stats()
        self.restart_game()

    def game_lost(self):
        st.error(f"Game over. The correct country was '{self.get_current_country()['name']}'.")
        self.set_game(st.session_state.level)
        self.restart_game()

    def restart_game(self):
        if st.button("Reset Game 🔁"):
            self.set_game(st.session_state.level)
    
    def update_stats(self):
        st.session_state.total_score += st.session_state.score
        if st.session_state.score > st.session_state.highscore:
            st.session_state.highscore = st.session_state.score
            st.session_state.gewinner = "Current Player"
        self.find_average_score()
    
    def find_average_score(self):
        try:
            st.session_state.average_score = st.session_state.total_score / st.session_state.right_guesses
        except ZeroDivisionError:
            st.session_state.average_score = st.session_state.total_score
    
    def calculate_average_guesses(self):
        try:
            return st.session_state.total_guesses / st.session_state.right_guesses
        except ZeroDivisionError:
            return st.session_state.total_guesses
    