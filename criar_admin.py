from models import session, User
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(['123123']).generate()[0]
usuario = User(nome='thiago', email='thiago@gmail.com', senha=senha_criptografada, admin=True)
session.add(usuario)
session.commit()      