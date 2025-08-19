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


base_fechados = dados[dados["Status"].isin(["Finalizado", "Em andamento"])]

andamento = dados[dados["Status"] == "Em andamento"]

card('oportunidades.png', f'{dados['Código Projeto'].count():,}', 'Oportunidades', coluna_esquerda)
card('projetos_fechados.png', f'{base_fechados['Código Projeto'].count():,}', 'Projetos Fechados', coluna_meio)
card('em_andamento.png', f'{andamento['Código Projeto'].count():,}', 'Em Andamento', coluna_direita)

card('total_pago.png', f'R${base_fechados["Valor Orçado"].sum():,}', 'Total Orcado', coluna_esquerda)
card('total_pago.png', f'R${base_fechados["Valor Negociado"].sum():,}', 'Total Pago', coluna_direita)
card('desconto.png', f'R${base_fechados["Desconto Concedido"].sum():,}', 'Total Desconto', coluna_meio)



import plotly.express as px

dados_grafico_funil = dados.groupby('Status', as_index=False).count()
dados_grafico_funil = dados_grafico_funil.rename(columns={'Código Projeto': 'Quantidade'})
dados_grafico_funil = dados_grafico_funil.sort_values(by='Quantidade', ascending=False)



grafico = px.funnel(dados_grafico_funil, x='Quantidade', y='Status')


st.plotly_chart(grafico)
