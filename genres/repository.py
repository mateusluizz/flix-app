import requests
import streamlit as st
from constants import BASE_URL
from login.service import logout


class GenreRepository:

    def __init__(self) -> None:
        self.__base_url = BASE_URL
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Error fetching API data. \
            Message: {response.json()} \
            Status code:  {response.status_code}'
        )

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            f'Error fetching API data. \
            Message: {response.json()} \
            Status code:  {response.status_code}'
        )
