import streamlit as st
from carregar_dados import carregar_dados
import plotly.express as px

st.title('DashBoards')

base = carregar_dados()
coluna_esquerda, coluna_direita, coluna_meio = st.columns([1, 1, 1])




setor = coluna_esquerda.selectbox('Setor', list(base['Setor'].unique()))
status = coluna_meio.multiselect('Status', options=list(base['Status'].unique()))

base = base[(base['Setor'] == setor) & (base['Status'].isin(status))]

container =  st.container(border=True)


base_mensal = base.groupby(
    base['Data Chegada'].dt.to_period('M')).sum(numeric_only=True).reset_index()

base_mensal['Data Chegada'] = base_mensal['Data Chegada'].dt.to_timestamp()




base['Data Chegada Mês'] = base['Data Chegada'].dt.to_period('M')
base_mensal_status = (
    base.groupby(['Data Chegada Mês', 'Status'])
        .sum(numeric_only=True)
        .reset_index()
)
# Converter período de volta para timestamp para plotar
base_mensal_status['Data Chegada'] = base_mensal_status['Data Chegada Mês'].dt.to_timestamp()


with container:
    
    #grafico de area
    st.write('### Total de Projetos por mes (R$)')

    grafico_area = px.area(base_mensal_status, x='Data Chegada', y='Valor Negociado', color='Status')

    st.plotly_chart(grafico_area)


    #grafico de coluna
    #grafico_barra = px.bar(base_mensal)
    st.write('### Comparação Orçado X Pago')
    coluna_esquerda, coluna_direita = st.columns([1, 1])

    #ano
    base_mensal['Ano'] = base_mensal['Data Chegada'].dt.year
    lista_de_anos = list(base_mensal['Ano'].unique())
    ano_selecionado = coluna_direita.selectbox(lista_de_anos)

    #st.plotly_chart(grafico_barra)