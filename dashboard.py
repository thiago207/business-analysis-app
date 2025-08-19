import streamlit as st
from carregar_dados import carregar_dados
import plotly.express as px

st.title('DashBoards')

base = carregar_dados()
coluna_esquerda, coluna_direita, coluna_meio = st.columns([1, 1, 1])




setor = coluna_esquerda.selectbox('Setor', list(base['Setor'].unique()))
status = coluna_meio.selectbox('Status', list(base['Status'].unique()))

base = base[(base['Setor'] == setor) & (base['Status'] == status)]

container =  st.container(border=True)

base_mensal = base.groupby(base['Data Chegada'].dt.to_period('M')).sum(numeric_only=True)


with container:

    #grafico de area
    st.write('### Total de Projetos por mes (R$)')

    grafico_area = px.area(base, x='Data Chegada', y='Valor Negociado')

    st.plotly_chart(grafico_area)

    #grafico de coluna