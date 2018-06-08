from model.orm import Base, engine

# Você precisa informar as classes que representam tabelas
from model.model import Produto, ItemVenda, Venda

print('Dropping database ...')
# apagando o BD
Base.metadata.drop_all(engine)

print('Creating database ...')
# criando o BD
Base.metadata.create_all(engine)

print('Database is done!')
