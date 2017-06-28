
class Produto(object):
    def __init__(self, pId, pNome, pVrCusto, pVrVenda):
        self.id = pId
        self.nome = pNome
        self.valor_custo = pVrCusto
        self.valor_venda = pVrCusto

class ItemVenda(object):
    def __init__(self):
        self.produto = None
        self.quantidade = 0

    def setProduto(self, pProduto, pQtde=1):
        if not pProduto:
            raise Exception('O produto não foi informado.')

        self.produto = pProduto
        self.quantidade = pQtde

    def subTotal(self):
        return self.quantidade * self.produto.valor_venda

class Venda(object):
    def __init__(self):
        self.itens = {}
        self.desconto = 0.00

    def valorTotal(self):
        vt = 0.00

        for i in self.itens:
            vt =+ i.subTotal

        vt =- self.desconto

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

        elif self.itens[pIdProduto].quantidade = pQtde:
            del self.itens[pIdProduto]

        else:
            self.itens[pIdProduto].quantidade =- pQtde

    def getItens(self):
        li = ()

        for i in self.itens:
            li.add(i.produto.id, i.produto.valor_venda, i.quantidade)

        return li

