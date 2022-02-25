from db import session, addRegisters, startDatabase, createNewDB, saveSession
from datetime import datetime
from model import Cliente, Endereco

class App(object):
    def __init__(self):
        startDatabase()

    def addCliente(self, pNome, pDtNascimento, pCpf, pLogradouro, pNum,
        pBairro, pCidade, pEstado):
        c = Cliente(nome=pNome, dtNascimento=pDtNascimento, cpf=pCpf)
        c.endereco = [Endereco(logradouro=pLogradouro, numero=pNum, bairro=pBairro,
                     cidade=pCidade, estado=pEstado, cliente_id=c.id)]
        addRegisters([c])
        saveSession()

    def getCliente(self, idCliente):
        c = session.query(Cliente).filter(Cliente.id==idCliente).first()
        return c

    def getClientes(self):
        c = session.query(Cliente).all()
        return c 

    def getClientesPorNome(self, nome):
        c = session.query(Cliente).filter(Cliente.nome.ilike('%'+ nome +'%')).all()
        return c 

    def delCliente(self, idCliente):
        c = self.getCliente(idCliente)
        
        if not c:
            msg_err = "O Cliente com ID {0} não foi encontrado.".format(idCliente)
            raise Exception(msg_err)
        
        session.delete(c)
        saveSession()

    
    def recriarBanco(self):
        createNewDB()

if __name__ == "__main__":
     
    print("\n---- Instanciando a aplicação ----")
    app = App()

    # a linha abaixo serve para recriar o BD. 
    app.recriarBanco()

    print("\n---- Adicionando um cliente ----")
    app.addCliente("Danilo", datetime(2003, 3, 20), '11122233344',
                    "rua", "0", "bairro", "cidade", "MG")
    
    print("\n---- Pesquisando e imprimindo os dados do cliente ----")
    c = app.getCliente(1)
    print(c)

    cs = app.getClientesPorNome("ni")
    for c in cs:
        print(c)

    # print("\n---- Deletando os dados do cliente ----")
    app.delCliente(1)
    cs = app.getClientes()
    for c in cs:
        print(c)
