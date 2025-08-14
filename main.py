import streamlit as st
import pandas as pd


@st.cache_data
def carregar_dados(dados):
    tabela = pd.read_csv("Base.xlsx")
    return tabela



st.title('Projeto Analise Empresarial')
st.write("Bem vindo, ...")

