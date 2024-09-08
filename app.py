import streamlit as st
from actors.page import show_actors
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews


def main():

    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Select an option',
            ['Home', 'Genres', 'Actor/Actress', 'Movies', 'Reviews']
        )

        if menu_option == 'Home':
            show_home()
        elif menu_option == 'Genres':
            show_genres()
        elif menu_option == 'Actor/Actress':
            show_actors()
        elif menu_option == 'Movies':
            show_movies()
        elif menu_option == 'Reviews':
            show_reviews()


if __name__ == "__main__":
    main()
