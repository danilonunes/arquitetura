from app import db
from app.model.model import Produto, Venda, ItemVenda

db.drop_all()
db.create_all()

tx_lucro = 0.4

p1 = Produto(nome='Camiseta', vrCusto=28.00, vrVenda=28.00*tx_lucro+28.00)
p2 = Produto(nome='Calça', vrCusto=73.50, vrVenda=73.50*tx_lucro+73.50)
p3 = Produto(nome='Blusa', vrCusto=18.90, vrVenda=18.90*tx_lucro+18.90)
p4 = Produto(nome='Bermuda', vrCusto=36.42, vrVenda=36.42*tx_lucro+36.42)

#db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.commit()

iv1 = ItemVenda(produto=p1, qtde=3, vrVenda=28.00*tx_lucro+28.00)
print(iv1)

iv2 = ItemVenda(produto=p3, qtde=1, vrVenda=36.42*tx_lucro+36.42)
print(iv2)

v = Venda()
v.itens.append(iv1)
v.itens.append(iv2)

db.session.add(v)
db.session.commit()

print(Produto.query.all())

print(ItemVenda.query.all())
