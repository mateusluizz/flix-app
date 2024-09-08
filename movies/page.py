from datetime import datetime
from time import sleep
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():

    movies_service = MovieService()
    movies = movies_service.get_movies()

    genres_service = GenreService()
    genres = genres_service.get_genres()

    actor_service = ActorService()
    actors = actor_service.get_actors()

    if movies:
        st.title('Lista de filmes')

        movies_df: pd.DataFrame = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])

        gb = GridOptionsBuilder.from_dataframe(movies_df)
        gb.configure_column(
            'release_date',
            header_name="Data (DD-MM-YYYY)",
            type=["dateColumnFilter", "customDateTimeFormat"],
            custom_format_string='dd-MM-yyyy'
        )
        grid_options = gb.build()

        AgGrid(
            data=movies_df,
            gridOptions=grid_options,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme foi encontrado.')

    st.title("Cadastrar novo filme")
    title = st.text_input('Título do filme')
    release_date = st.date_input(
        "Data de Nascimento",
        min_value=datetime(1930, 1, 1),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    # Genres
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(
        'Gênero',
        list(genre_names.keys()),
    )

    # Actors
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_name]

    resume = st.text_area(
        'Resumo'
    )

    if st.button("Cadastrar"):
        new_movie = movies_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume
        )
        if new_movie:
            st.success(f'Filme {title} criado com sucesso!')
            sleep(2)
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos')
