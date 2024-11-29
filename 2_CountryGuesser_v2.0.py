#To do list:
#Hits food, color of flag etc (las pistas actuales son muy basicas, estas pistas deberian estar en un documento aparte con la base de datos de los paises)
#countries and flags on the main page as aesthetic
#Cutting down the ammount of countries and trials (la bse de datos es muy grande, pero no es algo que este contenido en el codigo actual)
#adding an adventurer that gives hints: emoji guy with hat that gives the hint at the beginning (sino el juego es poco intuitivo) #"OK, let’s start! Here are some easy countries for you..." (and maybe a hint, like the continent: "Think about [continent]"
#agregar la barra con los espacios de las letras: algo asi como "space_letters": ["_" for _ in word]
#adding an adventurer that gives hints: emoji guy with hat that gives the hint at the beginning (sino el juego es poco intuitivo) #"OK, let’s start! Here are some easy countries for you..." (and maybe a hint, like the continent: "Think about [continent]"
#agregar la barra con los espacios de las letras: algo asi como "space_letters": ["_" for _ in word]
#quiero que todo el juego este contenido en una sola class que se llame CountryGuesser
#Display (quiero que tenga una funcion que sea display y contenga todo lo que sea display)
#Quiero agregar dos def como estas: def game_won(self):



import streamlit as st
import random
from Data import (
    countries_all, countries_mid, countries_easy, countries_hard, 
    countries_south_america, countries_oceania, countries_north_america, 
    countries_africa, countries_europe, countries_asia
)

#Display

st.title("Welcome to CountryGuesser! 🌎")

# Adventurer Character

st.write("Select a difficulty to start your adventure:")
# Difficulty selection

difficulty = st.radio("Select difficulty", ["easy", "mid", "hard"])

#Hints system
# Function to get a random country with its hints
def get_random_country(difficulty):
    if difficulty == "easy":
        countries = countries_easy
    elif difficulty == "mid":
        countries = countries_mid
    else:
        countries = countries_hard

    country = random.choice(countries)
    return country

#Buttons Difficulty
col1, col2, col3, space2, hints = st.columns([.6,.755,1,.5,1])
with col1:
    if st.button("Easy 🧑‍🦽‍➡️"):
        st.session_state.wrong_guesses = 0
        st.write(st.session_state.random_country_easy)
        st.session_state.level = "1"
        #st.write(f"{st.session_state.level}")
with col2:
    if st.button("Medium 🏃‍➡️"):
        st.session_state.wrong_guesses = 0
        #st.write(st.session_state.random_country_mid)
        st.session_state.level = "2"
        #st.write(f"{st.session_state.level}")
with col3:
    if st.button("Hard 🏋️‍♀️"):
        st.session_state.wrong_guesses = 0
        #st.write(st.session_state.random_country_hard)
        st.session_state.level = "3"
        #st.write(f"{st.session_state.level}")

#Botones hints
subcol1, subcol2 = st.columns([4,1])
with subcol1:
    st.subheader("Choose your difficulty")
with subcol2:
    st.subheader("🤠")


#agregar el boton de reset

#if st.button("Reset Game"):
#    self.set_game() 

#agregar game won/lost




# Start the game if difficulty is selected
if difficulty:
    # Get a random country based on selected difficulty
    country = get_random_country(difficulty)

    # Initialize game state
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
        st.session_state.guessed_correctly = False
    
    # Show the first clue: Fun Fact
    if st.session_state.attempts == 0:
        st.write(f"**Fun fact:** {country['fact']}")



#Session state variables

if "wrong_guesses" not in st.session_state:
    st.session_state.wrong_guesses = 0

if "number_of_guesses" not in st.session_state:
    st.session_state.number_of_guesses = []

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

if "level" not in st.session_state:
    st.session_state.level = 0


# total guesses
if "total_guesses" not in st.session_state:
    st.session_state.total_guesses = 0
# correct guesses
if "right_guesses" not in st.session_state:
    st.session_state.right_guesses = 0
# score mechanic
if "score" not in st.session_state:
    st.session_state.score = 1566
if "highscore" not in st.session_state:
    st.session_state.highscore = 0
if "gewinner" not in st.session_state:
    st.session_state.gewinner = ""
if "average_score" not in st.session_state:
    st.session_state.average_score = 0
if "total_score" not in st.session_state:
    st.session_state.total_score = 0


#Stats functions
def find_average_score():
    try:
        st.session_state.average_score = st.session_state.total_score / st.session_state.right_guesses
    except:
        st.session_state.average_score = st.session_state.total_score

def checkhighscore():
    global gewinner, total_score
    st.session_state.total_score = st.session_state.total_score + st.session_state.score
    if st.session_state.score > st.session_state.highscore:
        st.session_state.highscore = st.session_state.score
        st.session_state.gewinner = username
    else:
        st.session_state.highscore = st.session_state.highscore


#Una verga la funcion. La idea es que haya un boton para reiniciar
#Seria como un reset_game
def recompute():

    st.session_state.random_country_easy = random.choice(countries_easy)
    st.session_state.random_country_mid = random.choice(countries_mid)
    st.session_state.random_country_hard = random.choice(countries_hard)
    st.session_state.right_guesses = st.session_state.right_guesses + 1
    st.session_state.score = 0
    find_average_score()


#revisar esta verga
if "random_country_easy" not in st.session_state:
    st.session_state.random_country_easy = random.choice(countries_easy)
if "random_country_mid" not in st.session_state:
    st.session_state.random_country_mid = random.choice(countries_mid)
if "random_country_hard" not in st.session_state:
    st.session_state.random_country_hard = random.choice(countries_hard)

right_country = st.session_state.random_country_easy
right_country1 = st.session_state.random_country_mid
right_country2 = st.session_state.random_country_hard



user_guess = st.chat_input("Enter your guess")

if user_guess:
    try:
        if st.session_state.level == "1":
            country = st.session_state.random_country_easy
            if user_guess in countries_easy:
                st.write(f"{user_guess}")
                st.session_state.total_guesses += 1
                st.session_state.all_easy += 1
                if user_guess == country["name"]:
                    st.write(f"Correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    st.session_state.score *= 1.3
                    st.session_state.guesses_easy += 1
                    st.write(f"{username}'s Score: {st.session_state.score:.0f}")
                    checkhighscore()
                    recompute()
                else:
                    st.write("No correct")
                    st.session_state.wrong_guesses += 1
                    st.session_state.score -= 3

                # Show clues based on wrong guesses
                if st.session_state.wrong_guesses == 2:
                    st.write(f"**Typical food:** {country['food']}")
                elif st.session_state.wrong_guesses == 4:
                    st.write(f"**Language:** {country['language']}")
                elif st.session_state.wrong_guesses == 6:
                    st.write(f"**Flag emoji:** {country['emoji']}")

            elif user_guess in countries_mid or user_guess in countries_hard:
                st.write("Too hard")
                st.session_state.wrong_guesses += 1
                st.session_state.score -= 3
            else:
                st.write("Please guess a Country")

        elif st.session_state.level == "2":
            country = st.session_state.random_country_mid
            if user_guess in countries_mid:
                st.write(f"{user_guess}")
                st.session_state.total_guesses += 1
                st.session_state.all_mid += 1
                if user_guess == country["name"]:
                    st.write(f"Correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    st.session_state.score *= 1.4
                    st.session_state.guesses_mid += 1
                    st.write(f"{username}'s Score: {st.session_state.score:.0f}")
                    checkhighscore()
                    recompute()
                else:
                    st.write("No correct")
                    st.session_state.wrong_guesses += 1
                    st.session_state.score -= 3

                # Show clues based on wrong guesses
                if st.session_state.wrong_guesses == 2:
                    st.write(f"**Typical food:** {country['food']}")
                elif st.session_state.wrong_guesses == 4:
                    st.write(f"**Language:** {country['language']}")
                elif st.session_state.wrong_guesses == 6:
                    st.write(f"**Flag emoji:** {country['emoji']}")

            elif user_guess in countries_easy or user_guess in countries_hard:
                st.write("Too easy" if user_guess in countries_easy else "Too hard")
                st.session_state.wrong_guesses += 1
                st.session_state.score -= 3
            else:
                st.write("Please guess a Country")

        elif st.session_state.level == "3":
            country = st.session_state.random_country_hard
            if user_guess in countries_hard:
                st.write(f"{user_guess}")
                st.session_state.total_guesses += 1
                st.session_state.all_hard += 1
                if user_guess == country["name"]:
                    st.write(f"Correct and it only took {st.session_state.wrong_guesses} wrong guess(es)")
                    st.session_state.wrong_guesses = 0
                    st.session_state.score *= 1.6
                    st.session_state.guesses_hard += 1
                    st.write(f"{username}'s Score: {st.session_state.score:.0f}")
                    checkhighscore()
                    recompute()
                else:
                    st.write("No correct")
                    st.session_state.wrong_guesses += 1
                    st.session_state.score -= 3

                # Show clues based on wrong guesses
                if st.session_state.wrong_guesses == 2:
                    st.write(f"**Typical food:** {country['food']}")
                elif st.session_state.wrong_guesses == 4:
                    st.write(f"**Language:** {country['language']}")
                elif st.session_state.wrong_guesses == 6:
                    st.write(f"**Flag emoji:** {country['emoji']}")

            elif user_guess in countries_easy or user_guess in countries_mid:
                st.write("Too easy" if user_guess in countries_easy else "Too hard")
                st.session_state.wrong_guesses += 1
                st.session_state.score -= 3
            else:
                st.write("Please guess a Country")

        else:
            st.write("Please select a difficulty")
    
    except ValueError:
        st.write("**Bot**: Please enter a valid number.")
else:
    st.write("")

#st.write(f"{st.session_state.highscore:.0f}")
#st.write(f"{st.session_state.gewinner}")
#st.write(f"{st.session_state.total_score:.0f}")
#st.write(f"{st.session_state.average_score:.0f}")
#st.write(f"{st.session_state.right_guesses}")
#st.write(f"{st.session_state.wrong_guesses}")

