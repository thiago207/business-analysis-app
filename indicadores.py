import streamlit as st
from carregar_dados import carregar_dados 
st.title('Indicadores')

dados = carregar_dados()

st.table(dados.head(5))

def card(icone, numero, texto, coluna_card):
    conteiner = coluna_card.container(border=True)