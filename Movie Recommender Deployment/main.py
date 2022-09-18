import streamlit as st
import pickle
import requests


def bring_poster(movie):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=cc64afb91be363fe46af380754cda801'.format(movie))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    movie_list = ranked_table[movie_index][0:7]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(bring_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.title("Movie Recommender")
movies = pickle.load(open("movies.pkl", 'rb'))
movies_list = movies['title'].values
selected_movie = st.selectbox("Choose your movie", movies_list)

ranked_table = pickle.load(open("ranked_table.pkl", 'rb'))

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
