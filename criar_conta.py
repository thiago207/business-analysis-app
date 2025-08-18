import streamlit as st
from models import session, User
import streamlit_authenticator as stauth

form = st.form('form_criar_conta')
nome_user = form.text_input('Nome do usuario')  
email_user = form.text_input('Email do usuario')  
senha_user = form.text_input('Senha do usuario', type='password')  
admin_user = form.checkbox('É um admin? ')
botao_submit = form.form_submit_button('Enviar')

if botao_submit:
    lista_user_existentes = session.query(User).filter_by(email=email_user).all()
    
    if len(lista_user_existentes) > 0: 
        st.write('Ja existe conta cadrastada com esse Email')

    elif len(email_user) < 5 or len(senha_user) < 3:
        st.write('Preencha corretamente os dados')

    senha_criptografada = stauth.Hasher([senha_user]).generate()[0]
    usuario = User(nome=nome_user, email=email_user, senha=senha_criptografada, admin=admin_user)
    session.add(usuario)
    session.commit()    