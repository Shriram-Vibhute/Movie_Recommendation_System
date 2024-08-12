# Importing required libraries
import pandas as pd
import pickle
import streamlit as st
import requests
from time import sleep


# Data loading in the form of dictonary and transforming into dataframe
load_data = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(load_data)
similarities = pickle.load(open('similarities_matrix.pkl', 'rb'))


# Fetching Movie Posters
def fetch_poster(movie_id: int, retries: int = 3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            poster_path = data.get('poster_path')
            
            if poster_path:
                full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
                return full_path
            else:
                return "Poster not available"
        
        except requests.RequestException as e:
            print(f"Request failed: {e}. Retrying ({attempt + 1}/{retries})...")
            sleep(2)  # Wait before retrying
    
    return "Failed to fetch poster"


# Fetching movies recommendation
def recommendation(Movie: str):

    movie_names = []
    movie_posters = []

    # Fetching the index of provided movie
    movie_idx = movies[movies['title'] == Movie].index[0]

    # Fetching simiarity scores
    distances = similarities[movie_idx]

    # Finding the top 10 movies having highest similarities
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda i: i[1])[1:11] # 0 belongs to self similarity

    for i in movie_list:
        poster = fetch_poster(movies.iloc[i[0]]['movie_id'])
        if poster != "Failed to fetch poster" and poster != "Poster not available":
            movie_names.append(movies.iloc[i[0]]['title'])
            movie_posters.append(poster)
    
    return movie_names, movie_posters


# Title
st.title('MOVIE RECOMMENDATION SYSTEM')

# Input box
selected_movie_name = st.selectbox(
    "Type/Select Movie from options",
    movies['title'].values
) # selected_movie_name have the name of movie which is selected

# Recommendation function
if st.button("Search"):
    movie_names, movie_posters = recommendation(selected_movie_name)

    columns_1 = st.columns(5)
    columns_2 = st.columns(len(movie_posters) - 5)

    for i in range(5):
        with columns_1[i]:
            st.text(movie_names[i])
            st.image(movie_posters[i])
    
    for i in range(len(movie_posters) - 5):
        with columns_2[i]:
            st.text(movie_names[5 + i])
            st.image(movie_posters[5 + i])