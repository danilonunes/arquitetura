'''
*************************************************
*              IFNMG - Campus Januária          *
*                       TADS                    *
*              Arquitetura de Software          *
*************************************************

Servidor de venda XML-RPC em Python 3 usando MVC.

'''

__project_name__ = 'IFNMG - Januária - TADS - Arquitetura de Software'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2017-06-28T10:47:57.531741'
__source__ = 'https://github.com/danilonunes/arquitetura/tree/master/python/exemplos/xmlrpc'

print("\nIniciando o AppServer ...")

from controller import CtrlEstoque
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from datetime import datetime

PORTA = 8999
server = SimpleXMLRPCServer(("localhost", PORTA), allow_none=True)

ce = CtrlEstoque() # intanciando o controlador

def addProduto(pNome, pVrCusto, pVrVenda):
    ce.addProduto(pNome, pVrCusto, pVrVenda)

def listaProdutos():
    return ce.listaProdutos()

def iniciarVenda():
    ce.iniciarVenda()

def addProdutoVenda(pIdProduto, pQtde):
    ce.addProdutoVenda(pIdProduto, pQtde)

def setDesconto(pDesconto):
    ce.setDesconto(pDesconto)

def getTotalVenda():
    return ce.getTotalVenda()

def finalizaVenda():
    ce.finalizaVenda()

def getItensVendaCorrente():
    return ce.getItensVendaCorrente()

def getlistaVendas(pDtInicio, pDtFim):
    try:
        dtInicio = datetime.strptime(str(pDtInicio), '%Y%m%dT%H:%M:%S')
        dtFim = datetime.strptime(str(pDtFim), '%Y%m%dT%H:%M:%S')

        lv = []
        for v in ce.listaVendas(dtInicio, dtFim):
            lv.append((v[0], v[1], xmlrpc.client.DateTime(v[2])))

        return (lv)
    except Exception as e:
        print('[ERRO]:\n{0}'.format(e))
        raise



# registrando as funções do controlador (interface)
server.register_function(listaProdutos, "listaProdutos")
server.register_function(addProduto, "addProduto")
server.register_function(iniciarVenda, "iniciarVenda")
server.register_function(addProdutoVenda, "addProdutoVenda")
server.register_function(setDesconto, "setDesconto")
server.register_function(getTotalVenda, "getTotalVenda")
server.register_function(finalizaVenda, "finalizaVenda")
server.register_function(getItensVendaCorrente, "getItensVendaCorrente")
server.register_function(getlistaVendas, "getlistaVendas")

print("Servidor ativo na porta {0}".format(PORTA))
print("Pressione CTRL+C para desativá-lo")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Servidor desativado.\n")
    exit(0)
except:
    print("Ocorreu um erro desconhecido.\n[ERRO]:\n")
    raise
