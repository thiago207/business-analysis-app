import streamlit as st

#containers
#columns

coluna_esquerda, coluna_direita = st.columns([1.2, 2])


with coluna_esquerda:
    st.title("App Empresarial")
    st.write("Bem vindo, Thiago!")  # aqui você pode usar o nome do login
    botao_dashboard = st.button("Dashboards Projeto")
    botao_indicadores = st.button("Indicadores Projeto")

with coluna_direita:
    
    st.image('imagens/home_png.png')

if botao_dashboard:
    st.switch_page('dashboard.py')

elif botao_indicadores:
    st.switch_page('indicadores.py')   
