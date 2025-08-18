import streamlit as st
import pandas as pd


@st.cache_data
def carregar_dados():
    tabela = pd.read_excel(r"C:\Users\Pichau\Documents\estudos\projeto-analise-empresarial-app\business-analysis-app\Base.xlsx")
    return tabela

