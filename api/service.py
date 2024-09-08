import requests
from constants import BASE_URL


class Auth:

    def __init__(self) -> None:
        self.__base_url = BASE_URL
        self.__auth_url = f"{self.__base_url}auth/token/"

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {
            'error': f'Error in auhtentication. \
            Message: {auth_response.json().get('detail')} \
            Status code: {auth_response.status_code}'
        }
