from time import sleep
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():

    review_service = ReviewService()
    reviews = review_service.get_reviews()

    movie_service = MovieService()
    movies = movie_service.get_movies()

    if reviews:

        st.write('Lista de Avaliações')

        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    st.title("Cadastrar nova avaliação")

    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        'Estrelas',
        min_value=0,
        max_value=5,
        step=1
    )

    comment = st.text_area('Comentário')

    if st.button("Cadastrar"):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment
        )
        if new_review:
            st.success(f'Avaliação do filme {movie_titles[selected_movie_title]} criado com sucesso!')
            sleep(2)
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos')
