import xmlrpc.client
from datetime import datetime

class ClienteRPC(object):
    '''
        Cliente leve (thin client) usando RPC
    '''

    def __init__(self):
        self.server = xmlrpc.client.ServerProxy("http://localhost:7080")

    def addCliente(self, nome, dtNascimento, cpf, logradouro, num,
        bairro, cidade, estado):
        self.server.addCliente(nome, dtNascimento, cpf, logradouro,
            num, bairro, cidade, estado)

    def getCliente(self, idCliente):
        c = self.server.getCliente(idCliente)
        return c

    def getClientes(self):
        c = self.server.getClientes()
        return c 

    def getClientesPorNome(self, nome):
        c = self.server.getClientesPorNome(nome)
        return c 

    def delCliente(self, idCliente):
        c = self.server.delCliente(idCliente)

    def addProduto(self, descricao):
        p = self.server.addProduto(descricao)

    def getProdutos(self):
        p = self.server.getProdutos()
        return p

    def iniciarVenda(self, idCliente):
        idVenda = self.server.iniciarVenda(idCliente)
        return idVenda

    def addItemVenda(self, idVenda, idProduto, qtde, valor):
        self.server.addItemVenda(idVenda, idProduto, qtde, valor)

    def getVrTotalVenda(self, idVenda):
        vt = self.server.getValorTotalVenda(idVenda)
        return vt

    def finalizarVenda(self, idVenda):
        self.server.finalizarVenda(idVenda)


if __name__ == "__main__":
     
    print("\n---- Instanciando a aplicação ----")
    app = ClienteRPC()
    
    app.addProduto("Produto 1")
    app.addProduto("Produto 2")

    print("\n---- Adicionando um cliente ----")
    app.addCliente("Cliente 1", datetime(2003, 3, 20), '11122233344', 
                    "rua", "0", "bairro", "cidade", "MG")
    app.addCliente("Cliente 2", datetime(2008, 3, 10), '11188833344', 
                    "rua a", "1", "bairro", "cidade", "SP")
    
    print("\n---- Pesquisando e imprimindo os dados do cliente ----")
    c = app.getCliente(1)
    print(c)

    print("\n---- Pesquisando os dados do cliente por parte do nome ----")
    cs = app.getClientesPorNome("lie")
    print(cs)

    # print("\n---- Deletando os dados do cliente ----")
    #app.delCliente(1)
    #cs = app.getClientes()
    #print(cs)

    #print("\n---- Imprimindo os produtos ----")
    #pts = app.getProdutos()
    #print(pts)

    print("\n---- Nova venda ----")
    idVenda = app.iniciarVenda(1)
    print("\nId Venda: {}".format(idVenda))
    
    idProd1 = 1
    idProd2 = 2

    app.addItemVenda(idVenda, idProd1, 1, 10.0)
    print("Subtotal da venda {0}: {1}".format(idVenda, 
                                              app.getVrTotalVenda(idVenda)))

    app.addItemVenda(idVenda, idProd2, 3, 37.92)
    print("Subtotal da venda {0}: {1}".format(idVenda, 
                                              app.getVrTotalVenda(idVenda)))
    app.finalizarVenda(idVenda)
    print("Venda finalizada!")
