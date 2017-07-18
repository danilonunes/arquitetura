from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from orm import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    valor_custo = Column(Numeric)
    valor_venda = Column(Numeric)

    def __init__(self, pId, pNome, pVrCusto, pVrVenda):
        self.id = pId
        self.nome = pNome
        self.valor_custo = pVrCusto
        self.valor_venda = pVrVenda

    def __repr__(self):
        return '<Produto(id={0}, nome=\"{1}\", valor_custo{2:.2f}, valor_venda={3:.2f})>'.format(self.id,
            self.nome, self.valor_custo, self.valor_venda)


class ItemVenda(Base):
    __tablename__ = 'item_venda'
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True)
    produto = relationship("Produto")
    venda_id = Column(Integer, ForeignKey('venda.id'), primary_key=True)
    venda = relationship("Venda", back_populates="itens")
    quantidade = Column(Float)

    def __init__(self):
        self.produto = None
        self.venda = None
        self.quantidade = 0

    def setProduto(self, pProduto, pQtde=1):
        if not pProduto:
            raise Exception('O produto não foi informado.')

        self.produto = pProduto
        self.quantidade = pQtde

    def subTotal(self):
        return self.quantidade * self.produto.valor_venda

    def __repr__(self):
        return '<ItemVenda(produto={0}, quantidade={1})>'.format(
            self.produto, self.quantidade)

class Venda(object):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    itens = relationship("ItemVenda",
                         primaryjoin="and_(Venda.id==ItemVenda.venda_id)")
    desconto = Column(Numeric)
    data_hora = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    def __init__(self):
        self.desconto = 0.00

    def valorTotal(self):
        vt = 0.00

        for i in self.itens:
            vt += self.itens[i].subTotal()

        vt -= self.desconto

        return vt

    def addItem(self, pProduto, pQtde=1):
        iv = ItemVenda()
        iv.setProduto(pProduto, pQtde)
        self.itens[pProduto.id] = iv

    def delItem(self, pIdProduto, pQtde=1):
        if not pIdProduto in self.itens:
            raise Exception('Produto não identificado na venda.')

        if self.itens[pIdProduto].quantidade < pQtde:
            raise Exception('A quantidade a ser removida é maior que a existente na venda.')

        elif self.itens[pIdProduto].quantidade == pQtde:
            del self.itens[pIdProduto]

        else:
            self.itens[pIdProduto].quantidade -= pQtde

    def getItens(self):
        return (self.itens)

    def __repr__(self):
        return '<Venda(itens={0}, desconto={1}, data_hora={2})>'.format(
            self.itens, self.desconto, str(self.data_hora))

# **************************** código de teste *********************************
# aqui verificamos se estamos executando esse arquivo ou usando-o como pacote
if __name__ == "__main__":
    #from orm import Session
    #s = Session()
    # CONTINUAR AQUI!!!!!!!!
    produtos = {}
    produtos[1] = Produto(1, 'Produto 1', 10.003, 17.00)
    produtos[2] = Produto(2, 'Produto 2', 20.006, 27.00)
    produtos[3] = Produto(3, 'Produto 3', 30.007, 37.00)
    produtos[4] = Produto(4, 'Produto 4', 40.002, 47.00)
    produtos[5] = Produto(5, 'Produto 5', 50.009, 57.00)
    produtos[6] = Produto(6, 'Produto 6', 60.006, 67.00)

    for p in produtos:
        print(produtos[p])

    vendas = {}
    v1_id = datetime.now()
    vendas[v1_id] = Venda()
    vendas[v1_id].addItem(produtos[1])
    vendas[v1_id].addItem(produtos[2])
    vendas[v1_id].addItem(produtos[3])
    vendas[v1_id].addItem(produtos[1])

    print(vendas[v1_id])
    print(vendas[v1_id].getItens())
