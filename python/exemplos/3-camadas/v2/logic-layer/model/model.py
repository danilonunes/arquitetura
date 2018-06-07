from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from orm import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    valor_custo = Column(Numeric)
    valor_venda = Column(Numeric)

    def __init__(self, pNome, pVrCusto, pVrVenda):
        # self.id = pId
        self.nome = pNome
        self.valor_custo = pVrCusto
        self.valor_venda = pVrVenda

    def __repr__(self):
        return '<Produto(id={0}, nome=\"{1}\", valor_custo={2:.2f}, valor_venda={3:.2f})>'.format(self.id,
            self.nome, self.valor_custo, self.valor_venda)


class ItemVenda(Base):
    __tablename__ = 'item_venda'
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True)
    produto = relationship("Produto")
    venda_id = Column(Integer, ForeignKey('venda.id'), primary_key=True)
    venda = relationship("Venda", back_populates="itens")
    quantidade = Column(Float)

    def __init__(self, pProduto, pVenda, pQtde=1):
        self.produto = pProduto
        self.venda = pVenda
        self.quantidade = pQtde

    def subTotal(self):
        return self.quantidade * self.produto.valor_venda

    def __repr__(self):
        return '<ItemVenda(produto={0}, quantidade={1})>'.format(self.produto,
            self.quantidade)

class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    itens = relationship("ItemVenda",
                         primaryjoin="and_(Venda.id==ItemVenda.venda_id)")
    desconto = Column(Numeric)
    data_hora = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self):
        self.desconto = 0.00
        # self.id = pId

    def valorTotal(self):
        vt = 0.00

        for i in self.itens:
            vt += self.itens[i].subTotal()

        vt -= self.desconto

        return vt

    def addItem(self, pProduto, pQtde=1):
        existe_prod = False
        for i in range(len(self.itens)):
            if self.itens[i].produto.id == pProduto.id:
                existe_prod = True
                break

        if existe_prod:
            self.itens[i].quantidade += pQtde
        else:
            iv = ItemVenda(pProduto, self, pQtde)
            self.itens.append(iv)

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

    # importando o objeto session do módulo orm
    from orm import session

    #id = 18
    #p = session.query(Produto).filter(Produto.id == id).all()
    #for p in session.query(Produto).filter(Produto.id == 19):
    #if p:
    #    print(p)
    #else:
    #    print("O produto com ID {0} não foi encontrado.".format(id))
    # produtos = {}
    # produtos[1] = Produto('Produto 1', 10.003, 17.00)
    # produtos[2] = Produto('Produto 2', 20.006, 27.00)
    # produtos[3] = Produto('Produto 3', 30.007, 37.00)
    # produtos[4] = Produto('Produto 4', 40.002, 47.00)
    # produtos[5] = Produto('Produto 5', 50.009, 57.00)
    # produtos[6] = Produto('Produto 6', 60.006, 67.00)
    #
    # # adicionando os produtos ao banco
    # try:
    #     for p in produtos:
    #         session.add(produtos[p])
    #         session.commit()
    # except Exception as e:
    #     session.rollback()
    #     raise e
    #
    # tam_linha = 60
    # linha = tam_linha * '*'
    #
    # # consultando e imprimindo todos os registro da tabela produto no BD
    # # consulta equivalente ao código SELECT * FROM produto
    # for p in session.query(Produto).all():
    #     print(linha)
    #     print(p)
    # print(linha)
    #
    # # consultando e imprimindo todos os registro da tabela produto no BD
    # # consulta equivalente ao código SELECT p.nome, p.valor_venda FROM produto as p
    # for nome, vr_venda in session.query(Produto.nome, Produto.valor_venda).all():
    #     print(linha)
    #     print('|', nome,'|', '{0:.2f}'.format(vr_venda), '|')
    # print(linha)
    #
    # v1 = Venda()
    # v1.addItem(produtos[1])
    # v1.addItem(produtos[2])
    # v1.addItem(produtos[3])
    # v1.addItem(produtos[1])
    #
    # # adicionando as vendas ao banco
    # try:
    #     session.add(v1)
    #     session.commit()
    # except Exception as e:
    #     session.rollback()
    #     raise e
    #
    # print(v1) # imprimindo a venda
    # print(v1.getItens()) # imprimindo os itens da venda

    from sqlalchemy.sql.expression import func

    max_id_produto = session.query(func.max(Produto.id)).all()[0][0]
    print("Maior ID de Produto: {0}".format(max_id_produto))
