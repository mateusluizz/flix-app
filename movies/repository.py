import requests
import streamlit as st
from constants import BASE_URL
from login.service import logout


class MovieRepository:

    def __init__(self) -> None:
        self.__base_url = BASE_URL
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
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

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return
        raise Exception(
            f'Error fetching API data. \
            Message: {response.json()} \
            Status code:  {response.status_code}'
        )

    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return
        raise Exception(
            f'Error fetching API data. \
            Message: {response.json()} \
            Status code:  {response.status_code}'
        )
