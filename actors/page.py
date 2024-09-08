from datetime import datetime
from time import sleep
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():

    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.title('Lista de Ator/Atriz')

        actors_df: pd.DataFrame = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key="actors_grid"
        )
    else:
        st.warning('Nenhum Ator/Atriz encontrado.')

    st.title("Cadastrar novo Ator/Atriz")

    name = st.text_input("Nome do(a) Ator/Atriz")
    birthday = st.date_input(
        "Data de Nascimento",
        min_value=datetime(1930, 1, 1),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality = st.selectbox(
        'Nacionalidade',
        ['US', 'BR']
    )

    if st.button("Cadastrar"):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.success(f'Ator/Atriz {name} criado com sucesso!')
            sleep(2)
            st.rerun()
        else:
            st.error("Erro ao cadastrar Ator/Atriz. Verifique os campos!")
