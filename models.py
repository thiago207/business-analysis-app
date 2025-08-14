from sqlalchemy import create_engine, Integer, String, Boolean, Column
from sqlalchemy.orm import create_session, declarative_base

db =  create_engine('sqlite:///datebase/meubanco.db')
Session = create_engine(bind=db)
session = Session()

Base = declarative_base()
#class User
    #id
    #nome
    #email
    #senha
    #admin
class User(Base):
    id = Column('id', Integer)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('id', String)
    adim = Column('adim', Boolean)




Base.metadata.create_all(bind=db)