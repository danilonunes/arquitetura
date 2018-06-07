from orm import Base, engine

# Você precisa informar as classes que representam tabelas 
from model import Produto, ItemVenda, Venda

# apagando o BD
Base.metadata.drop_all(engine)

# criando o BD
Base.metadata.create_all(engine)
