import streamlit as st
from carregar_dados import carregar_dados 
st.title('Indicadores')

dados = carregar_dados()


def card(icone, numero, texto, coluna_card):
    conteiner = coluna_card.container(border=True)

    coluna_esquerda, coluna_direita = conteiner.columns([1, 2])

    coluna_esquerda.image(f'imagens/{icone}')
    coluna_direita.write(numero)
    coluna_direita.write(texto)

coluna_esquerda, coluna_direita, coluna_meio = st.columns([1, 1, 1])

card('\oportunidades.png', '123', 'Oportunidades', coluna_esquerda)
card('\oportunidades.png', '123', 'Projetos Fechados', coluna_meio)
card('\oportunidades.png', '123', 'Em Andamento', coluna_direita)