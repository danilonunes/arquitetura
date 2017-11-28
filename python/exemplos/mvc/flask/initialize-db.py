from app import db

# Apaga todas as tabelas do banco de dados
db.drop_all()

# Cria todas as tabelas no banco de dados,
# aplicando a estrutura definida no Model.
db.create_all()
