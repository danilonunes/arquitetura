from model.model import Venda, Produto
from datetime import datetime
from model.orm import session
from sqlalchemy.sql.expression import func

class CtrlEstoque(object):
    def __init__(self):
        #self.__produtos = {} # atributo "privado"
        #self.__vendas = {} # atributo "privado"
        #self.__ultIdProduto = 0 # atributo "privado"
        self.__vendaCorrente = None # atributo "privado"

    def __getProduto(self, pId):
        p = session.query(Produto).filter(Produto.id == pId).all()[0]

        if not p:
            raise Exception('Produto com o identificador \"{0}\" não encontrado.'.format(pId))

        return p

# consultas
    def listaProdutos(self):
        produtos = []

        for p in session.query(Produto).order_by(Produto.id).all():

            produtos.append((p.id, p.nome, p.valor_custo, p.valor_venda))

        return (produtos) # retorna uma tupla

    def listaVendas(self, pDtInicio=datetime.today().date(),
        pDtFim=datetime.today().date()):

        vp = [] # instancia uma lista

        for v in session.query(Venda).order_by(Venda.id).\
            filter(func.date(Venda.data_hora) >= pDtInicio,
                func.date(Venda.data_hora) <= pDtFim).all():

                vp.append((v.id, v.desconto, v.data_hora))

        return (vp) # retorna uma tupla

# operações
    def addProduto(self, pNome, pVrCusto, pVrVenda):
        # p = Produto(self.__getIdNovoProduto(), pNome, pVrCusto,
        #     pVrVenda)
        try:
            p = Produto(pNome, pVrCusto, pVrVenda)
            session.add(p)
            session.commit()
            #self.__produtos[p.id] = p
        except Exception as e:
            session.rollback()
            raise e

    def iniciarVenda(self):
        if not self.__vendaCorrente:
            self.__vendaCorrente = Venda()

    def addProdutoVenda(self, pIdProduto, pQtde):
        if not self.__vendaCorrente:
            raise Exception('Não existe uma venda ativa.')

        if not pQtde:
            raise Exception("Quantidade \"{0}\" inválida.")

        p = self.__getProduto(pIdProduto)
        self.__vendaCorrente.addItem(p, pQtde)

    def setDesconto(self, pDesconto):
        if not self.__vendaCorrente:
            raise Exception('Não existe uma venda ativa.')

        self.__vendaCorrente.desconto = pDesconto

    def getTotalVenda(self):
        if not self.__vendaCorrente:
            raise Exception('Não existe uma venda ativa.')

        return self.__vendaCorrente.valorTotal()

    def finalizaVenda(self):
        if not self.__vendaCorrente:
            raise Exception('Não existe uma venda ativa.')

        # chave -> vendaCorrente.data_hora
        #self.__vendas[self.__vendaCorrente.data_hora] = self.__vendaCorrente
        try:
            session.add(self.__vendaCorrente)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

        self.__vendaCorrente = None

    def getItensVendaCorrente(self):
        if not self.__vendaCorrente:
            raise Exception('Não existe uma venda ativa.')

        itensVenda = []

        for i in self.__vendaCorrente.getItens():
            itensVenda.append(i.produto_id, i.venda_id, i.quantidade)

        return (itensVenda)

# **************************** código de teste *********************************
# aqui verificamos se estamos executando esse arquivo ou usando-o como pacote
if __name__ == "__main__":
    c = CtrlEstoque()
    c.addProduto('Produto 1', 10.003, 17.00)
    c.addProduto('Produto 2', 20.006, 27.00)
    c.addProduto('Produto 3', 30.007, 37.00)
    c.addProduto('Produto 4', 40.002, 47.00)
    c.addProduto('Produto 5', 50.009, 57.00)
    c.addProduto('Produto 6', 60.006, 67.00)

    lp = c.listaProdutos()
    for p in lp:
        print(p)

# ------------- venda -------------
    c.iniciarVenda()

    c.addProdutoVenda(1, 3)
    # print(c.getItensVendaCorrente())
    # print(c.getTotalVenda())

    c.addProdutoVenda(3, 1)
    # print(c.getItensVendaCorrente())
    # print(c.getTotalVenda())

    c.addProdutoVenda(5, 2)
    # print(c.getItensVendaCorrente())
    # print(c.getTotalVenda())

    c.setDesconto(2.5)
    print(c.getTotalVenda())

    c.finalizaVenda()
    print(c.listaVendas())
