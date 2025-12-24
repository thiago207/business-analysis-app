import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, User    


lista_de_user = session.query(User).all()

# CREDENCIAIS DO USUARIO:
credenciais = {
    'usernames': {
        str(u.email): {'name': u.nome, 'password': u.senha}
        for u in lista_de_user
    }
}

# AUTENTICADOR:
authenticator = stauth.Authenticate(
    credenciais, "credenciais_projeto", 'ad1231das#@#$%87**90', cookie_expiry_days=30
)


def autenticar_user(authenticator):
    # Evita criar o form de login mais de uma vez
    if "authentication_status" not in st.session_state:
        st.session_state.authentication_status = None
    
    if "name" not in st.session_state:
        st.session_state.name = None
    
    if "username" not in st.session_state:
        st.session_state.username = None

    # Só chama login se ainda não foi autenticado
    if st.session_state.authentication_status is None:
        try:
            authenticator.login()
        except Exception as e:
            st.error(f"Erro ao fazer login: {e}")
            return None

    # Verifica o status da autenticação
    if st.session_state.authentication_status:
        return {
            "nome": st.session_state.name,
            "username": st.session_state.username
        }
    elif st.session_state.authentication_status is False:
        st.error("Login ou senha incorretos.")
        return None
    else:
        st.warning("Preencha o formulário para entrar.")
        return None


dados_user = autenticar_user(authenticator)
if dados_user is None:
    st.stop()


def logout():
    authenticator.logout()
    # Limpa o session_state
    for key in list(st.session_state.keys()):
        del st.session_state[key]


if dados_user:
    email_user = dados_user['username']
    user = session.query(User).filter_by(email=email_user).first()

    if user.admin:
        pg = st.navigation({
            'Home': [st.Page('home.py', title='Home')],
            'Dashboards': [
                st.Page('dashboard.py', title='Dashboards'),
                st.Page('indicadores.py', title='Indicadores')
            ],
            'Conta': [
                st.Page(logout, title='Sair'),
                st.Page('criar_conta.py', title='Criar Conta')
            ]
        })
    else:
        pg = st.navigation({
            'Home': [st.Page('home.py', title='Home')],
            'Dashboards': [
                st.Page('dashboard.py', title='Dashboards'),
                st.Page('indicadores.py', title='Indicadores')
            ],
            'Conta': [st.Page(logout, title='Sair')]
        })

    pg.run()