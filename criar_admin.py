from models import session, User
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(['123123']).generate()[0]
usuario = User(nome='thiago2', email='thiago2@gmail.com', senha=senha_criptografada, admin=False)
session.add(usuario)
session.commit()      