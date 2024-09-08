import requests
import streamlit as st
from constants import BASE_URL
from login.service import logout


class ReviewRepository:

    def __init__(self) -> None:
        self.__base_url = BASE_URL
        self.__reviews_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_reviews(self):
        response = requests.get(
            self.__reviews_url,
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

    def create_review(self, review):
        response = requests.post(
            self.__reviews_url,
            headers=self.__headers,
            data=review
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

    def get_review_stats(self):
        response = requests.get(
            f'{self.__reviews_url}stats/',
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
