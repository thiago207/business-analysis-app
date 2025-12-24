import streamlit as st
import pandas as pd
import os


@st.cache_data
def carregar_dados():
    # Caminho relativo ao diretório do projeto
    caminho_base = os.path.join(os.path.dirname(__file__), "Base.xlsx")
    
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_base):
        st.error(f"Arquivo não encontrado: {caminho_base}")
        return pd.DataFrame()  # Retorna DataFrame vazio em caso de erro
    
    tabela = pd.read_excel(caminho_base)
    return tabela