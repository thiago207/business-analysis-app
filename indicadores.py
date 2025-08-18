import streamlit as st
from carregar_dados import carregar_dados 
st.title('Indicadores')

dados = carregar_dados()
