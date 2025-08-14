from models import session, User
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(['123123']).generate()
