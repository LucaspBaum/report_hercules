import streamlit as st
import pandas as pd

st.sidebar.markdown("Desenvolvido por Lucas Baumgartner. Revisado por Caio Knothe.")

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Instagram - Jogos')
    st.markdown('5743')

    st.header("CTR")
    st.markdown('77,6%')

    st.header('Instagram - Jogos finalizado')
    st.markdown('3058')

with col2:
    st.header('Telegram - Enviado')
    st.markdown('33')

    st.header('Telegram - Jogado')
    st.markdown('20')

    st.header('Telegram - Jogo finalizado')
    st.markdown('18')

with col3:
    st.header('Visitas ao site')
    st.markdown('1876')

    st.header('Inscrições')
    st.markdown('785')