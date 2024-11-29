import streamlit as st

# Lists of countries with difficulty categories 
countries_easy = [
    {"name": "Argentina", "food": "Asado", "language": "Spanish", "emoji": "🇦🇷", "fact": "This country is known for having the world's highest mountain outside of the Himalayas, Aconcagua."},
    {"name": "Australia", "food": "Vegemite", "language": "English", "emoji": "🇦🇺", "fact": "This country is the only one that is also a continent and has a unique marsupial called the kangaroo."},
    {"name": "Brazil", "food": "Feijoada", "language": "Portuguese", "emoji": "🇧🇷", "fact": "This country has a massive rainforest that is considered the 'lungs of the planet' due to its oxygen production."},
    {"name": "Canada", "food": "Poutine", "language": "English, French", "emoji": "🇨🇦", "fact": "This country has the longest coastline in the world and is known for its ice hockey."},
    {"name": "Belgium", "food": "Waffles", "language": "Dutch, French, German", "emoji": "🇧🇪", "fact": "This country is famous for its medieval towns, Renaissance architecture, and being the headquarters of the European Union."}
]

countries_mid = [
    {"name": "Honduras", "food": "Peking Duck", "language": "Mandarin", "emoji": "🇭🇳", "fact": "This country is home to one of the longest rivers in Central America and ancient Mayan ruins."},
    {"name": "Liechtenstein", "food": "Biryani", "language": "German", "emoji": "🇱🇮", "fact": "This small principality is known for its alpine landscapes and is bordered by Switzerland and Austria."},
    {"name": "Romania", "food": "Tacos", "language": "Romanian", "emoji": "🇷🇴", "fact": "This country is known for the legend of Dracula and its beautiful castles like Bran Castle."},
    {"name": "Slovenia", "food": "Biltong", "language": "Slovene", "emoji": "🇸🇮", "fact": "This country is known for its vast forests and beautiful lakes like Lake Bled."},
    {"name": "Thailand", "food": "Sushi", "language": "Thai", "emoji": "🇹🇭", "fact": "This country is famous for its Buddhist temples and stunning beaches."}
]

countries_hard = [
    {"name": "Nepal", "food": "Dal Bhat", "language": "Nepali", "emoji": "🇳🇵", "fact": "This country is home to the highest mountain in the world, Mount Everest, and a unique culture of mountain peoples."},
    {"name": "Latvia", "food": "Ravitoto", "language": "Latvian", "emoji": "🇱🇻", "fact": "This country is known for its rich medieval history and vast forests that cover much of the land."},
    {"name": "Fiji", "food": "Injera", "language": "Fijian, Hindi, English", "emoji": "🇫🇯", "fact": "This island nation is known for its tropical climate, coral reefs, and unique indigenous cultures."},
    {"name": "Antigua and Barbuda", "food": "Piri Piri Chicken", "language": "English", "emoji": "🇦🇬", "fact": "This Caribbean island nation is famous for its beaches and colorful colonial architecture."},
    {"name": "Bhutan", "food": "Ema Datshi", "language": "Dzongkha", "emoji": "🇧🇹", "fact": "This country is known for measuring success in terms of Gross National Happiness instead of GDP."}
]