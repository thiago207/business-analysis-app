import streamlit as st
from carregar_dados import carregar_dados 
st.title('Indicadores')

dados = carregar_dados()


def card(icone, numero, texto, coluna_card):
    conteiner = coluna_card.container(border=True)

    coluna_esquerda, coluna_direita = conteiner.columns([1, 1])
    
    coluna_esquerda.image(f'imagens/{icone}')

    coluna_esquerda.markdown(f"<h3 style='margin:0;'></h3>", unsafe_allow_html=True)
    coluna_direita.write(numero)
    coluna_direita.write(texto)

coluna_esquerda, coluna_direita, coluna_meio = st.columns([1, 1, 1])

card('oportunidades.png', '2633', 'Oportunidades', coluna_esquerda)
card('projetos_fechados.png', '504', 'Projetos Fechados', coluna_meio)
card('em_andamento.png', '331', 'Em Andamento', coluna_direita)

card('total_pago.png', 'R$10,489,500', 'Total Orcado', coluna_esquerda)
card('total_pago.png', 'R$9,625,100', 'Total Pago', coluna_meio)
card('desconto.png', 'R$864,400', 'Total Desconto', coluna_direita)

st.table(dados.head(15))