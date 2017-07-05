from datetime import datetime

class Produto(object):
    def __init__(self, pId, pNome, pVrCusto, pVrVenda):
        self.id = pId
        self.nome = pNome
        self.valor_custo = pVrCusto
        self.valor_venda = pVrVenda

    def __repr__(self):
        return '{0}, {1}, {2:.2f}, {3:.2f}'.format(self.id, self.nome,
            self.valor_custo, self.valor_venda)


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

    def __repr__(self):
        return '{0}, {1}'.format(self.produto, self.quantidade)

class Venda(object):
    def __init__(self):
        self.itens = {}
        self.desconto = 0.00
        self.data_hora = datetime.now()

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
        return '{0}, {1}, {2}'.format(self.itens, self.desconto, str(self.data_hora))

# **************************** código de teste *********************************
# aqui verificamos se estamos executando esse arquivo ou usando-o como pacote
if __name__ == "__main__":
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
