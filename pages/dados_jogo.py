import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Dados do Jogo",
    layout='wide'
)

df_fluxograma = pd.read_csv('dados_fluxograma.csv')

st.sidebar.markdown("Desenvolvido por Lucas Baumgartner. Revisado por Caio Knothe.")

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 50,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = df_fluxograma['Etapas'],
      
    ),
    link = dict(
      source = [0, 1, 2, 3, 4, 5, 6, 7, 8], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [1, 2, 3, 4, 5, 6, 7, 8, 8],
      value = df_fluxograma['Enviada']
  ))])

fig.update_layout(title_text="Fluxograma das etapas do jogo", title_font_size = 44, font_size=12, font_color = 'yellow')

st.plotly_chart(fig, use_container_width=True)