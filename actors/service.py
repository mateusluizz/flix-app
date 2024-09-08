import streamlit as st
from actors.repository import ActorRepository


class ActorService:
    def __init__(self) -> None:
        self.repository = ActorRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.repository.get_actors()
        st.session_state.actors = actors
        return actors

    def get_actors_name(self):
        genres = self.repository.get_actors()
        return [genre.get('name') for genre in genres]

    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        new_actor = self.repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
