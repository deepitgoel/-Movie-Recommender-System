import pandas as pd
import streamlit as st
import pickle
import requests

#loading the movies df
df = pd.read_pickle("movies_data.pkl")
movies_list = df['title'].values

##loading the similarity matrix
with open("similarity_matrix.pkl", "rb") as file:
    similarity =  pickle.load(file)


def recommend(movie):
  movie_idx = df[df['title'] == movie].index[0]
  sim = similarity[movie_idx]
  sim_movie_list = sorted(list(enumerate(sim)), reverse = True , key = lambda x : x[1])[1:6]

  rec_movie = []
  rec_movie_poster = []  
  for mov in sim_movie_list:
    rec_movie.append(df.iloc[mov[0]].title)
    rec_movie_poster.append(fetch_poster(df.iloc[mov[0]].id))

  return rec_movie , rec_movie_poster

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=834c86e23888276322981ab25f6c2c99&language=en-US')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


st.title("Movie Recommender System")

movie_name = st.selectbox(
    'Enter the movie you have watched',
    movies_list)

if st.button("Recommend"):
    name, poster = recommend(movie_name)
    
    col = st.columns(5)
    for i in range(len(st.columns(5))):
        with col[i]:
            st.write(name[i])
            st.image(poster[i])

    # with col2:
    #     st.header(name[1])
    #     st.image("https://static.streamlit.io/examples/dog.jpg")

    # with col3:
    #     st.header(name[1])
    #     st.image("https://static.streamlit.io/examples/owl.jpg")
    
    # with col4:
    #     st.header(name[1])
    #     st.image("https://static.streamlit.io/examples/owl.jpg")
    
    # with col5:
    #     st.header(name[1])
    #     st.image("https://static.streamlit.io/examples/owl.jpg")
    
    
    
    
    

