import streamlit as st
from genres.repository import GenreRepository


class GenreService:

    def __init__(self) -> None:
        self.repository = GenreRepository()

    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.repository.get_genres()
        st.session_state.genres = genres
        return genres

    def get_genres_name(self):
        genres = self.repository.get_genres()
        return [genre.get('name') for genre in genres]

    def create_genre(self, name):
        genre = dict(
            name=name
        )
        new_genre = self.repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre
