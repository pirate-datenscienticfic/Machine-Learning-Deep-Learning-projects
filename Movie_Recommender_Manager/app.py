import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=823502806b702f80897bc20e8420f1f6&language=en-US')

    data = response.json()
    # st.text(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# --- Movies recommendation function --------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 6]

    recommended_movies = []
    recommended_movies_poster = []
    for cnt in movies_list:
        movie_id = movies.iloc[cnt[0]].movie_id
        # --- Fetch poster from API -----
        recommended_movies_poster.append(fetch_poster(movie_id))

        recommended_movies.append(movies.iloc[cnt[0]].title)
    return recommended_movies, recommended_movies_poster


# --- Streamlit file importing the pickle file -----------

# movies_list = pickle.load(open('movies.pkl', 'rb'))
# movies_list = movies_list['title'].values

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Title of the sites --------------
st.title('Movie Recommender Manager')

# --- Box of streamlit -----------
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    # movies_list
    movies['title'].values
)

# --- Button of streamlit --------------
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    movies_columns = st.columns(5)
    for cont in range(len(movies_columns)):
        with movies_columns[cont]:
            st.text(names[cont])
            st.image(posters[cont])

# https://movieguess-by-shubham.herokuapp.com/
