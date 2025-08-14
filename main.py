import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth


senha_criptografada = stauth.Hasher(['1234', '123']).generate()

#CREDENCIAIS DO USUARIO:
credenciais = {
    'usernames': {
        'thiago@gmail.com': {'name': 'Thiago', 'password': senha_criptografada[0]},
        'login@gmail.com': {'name': 'Login', 'password': senha_criptografada[1]}
    }
}

#AUTENTICADOR:
authenticator = stauth.Authenticate(
    credenciais, "credenciais_projeto", 'ad1231das#@#$%87**90', cookie_expiry_days=30
    )


def autenticar_user(authenticator):
    nome, status_autenticacao, username = authenticator.login()

    if status_autenticacao:
        return {'nome': nome, 'username': username}
    elif status_autenticacao == False:
        st.error('Login ou senha errada.')
    else:
        st.error('Preencha o formulario')
    
def logout(authenticator):
    authenticator.logout()

#AUTENTICAR USER:
dados_user = autenticar_user(authenticator)


if dados_user:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel(r"C:\Users\Pichau\Documents\estudos\projeto-analise-empresarial-app\business-analysis-app\Base.xlsx")
        return tabela

    base = carregar_dados()

    st.title('Projeto Analise Empresarial')
    st.write(f"Bem vindo, ....")
    st.table(base.head(10))

