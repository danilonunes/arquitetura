
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

    def valorTotal(self):
        vt = 0.00
        
        for i in self.itens:
            vt =+ i.subTotal

        return vt
