from models import session, User
import streamlit_authenticator as stauth

# Versão atualizada do Hasher
senha_criptografada = stauth.Hasher.hash('123123')

usuario = User(
    nome='Admin',
    email='admin@gmail.com',
    senha=senha_criptografada,
    admin=True
)

session.add(usuario)
session.commit()

print("✅ Usuário admin criado com sucesso!")
print(f"Email: admin@gmail.com")
print(f"Senha: 123123")