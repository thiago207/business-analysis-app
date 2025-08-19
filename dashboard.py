import streamlit as st
from carregar_dados import carregar_dados
st.title('DashBoards')

base = carregar_dados()
coluna_esquerda, coluna_direita, coluna_meio = st.columns([1, 1, 1])




setor = coluna_esquerda.selectbox('Setor', list(base['Setor'].unique()))
status = coluna_meio.selectbox('Status', list(base['Status'].unique()))

base = base[(base['Setor'] == setor) & (base['Status'] == status)]

st.table(base.head(10))