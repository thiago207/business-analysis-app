import streamlit as st

#containers
#columns

coluna_esquerda, coluna_direita = st.columns([1, 1.5])

st.title('App Empresarial')
st.write(f'''
#### Bem vindo, nome! 
''')

botao_dashboard = st.button('Dashboards Projeto')

botao_indicadores = st.button('Indicadores Projeto')

if botao_dashboard:
    st.switch_page('dashboard.py')

elif botao_indicadores:
    st.switch_page('indicadores.py')   

coluna_direita.image('')