import streamlit as st
import pandas as pd
import webbrowser

df_fluxograma = pd.read_csv('dados_fluxograma.csv')

st.markdown("# Relatório final do Jogo Deuses e Heróis - Hércules")

st.sidebar.markdown("Desenvolvido por Lucas Baumgartner. Revisado por Caio Knothe.")

st.markdown(
    """
    O jogo "Deuses e Heróis - Hércules" foi uma automação para chat de Instagram no perfil do professor Clóvis de Barros Filho
    que tinha como objetivo primário aumentar o engajamento e melhorar a interação com os fãs. Como objetivo secundário, pretendíamos aumentar as vendas
    do curso homônimo.

    A automação ocorreu toda no começo do ano de 2024, dos dias 15 de janeiro até o dia 18 de fevereiro. Para divulgar o jogo foram feitos posts no feed do Instagram, postagem
    nos Stories, envio de Newsletter, divulgação nos grupos de WhatsApp e Telegram.

    Para acessar o restante do relatório, clicar nas páginas laterais.
    """
)