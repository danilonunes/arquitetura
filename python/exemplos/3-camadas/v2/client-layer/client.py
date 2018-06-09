'''
*************************************************
*              IFNMG - Campus Januária          *
*                       TADS                    *
*              Arquitetura de Software          *
*************************************************

Cliente de venda XML-RPC em Python 3.

'''

__project_name__ = 'IFNMG - Januária - TADS - Arquitetura de Software'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2017-06-28T10:47:57.531741'
__source__ = 'https://github.com/danilonunes/arquitetura/tree/master/python/exemplos/xmlrpc'

import xmlrpc.client
from datetime import datetime

with xmlrpc.client.ServerProxy("http://localhost:8999/", allow_none=True, use_datetime=True) as venda:
    print(venda)
    venda.addProduto('Produto 1', 10.003, 17.00)
    venda.addProduto('Produto 2', 20.006, 27.00)
    venda.addProduto('Produto 3', 30.007, 37.00)
    venda.addProduto('Produto 4', 40.002, 47.00)
    venda.addProduto('Produto 5', 50.009, 57.00)
    venda.addProduto('Produto 6', 60.006, 67.00)

    lp = venda.listaProdutos()
    for p in lp:
        print(p)

# ------------- venda -------------
    venda.iniciarVenda()

    venda.addProdutoVenda(1, 3)

    print(venda.getItensVendaCorrente())
    print(venda.getItensVendaCorrente())
    print(venda.getTotalVenda())

    venda.addProdutoVenda(3, 1)

    print(venda.getItensVendaCorrente())
    print(venda.getTotalVenda())

    venda.addProdutoVenda(5, 2)

    print(venda.getItensVendaCorrente())
    print(venda.getTotalVenda())

    venda.setDesconto(2.5)
    print(venda.getTotalVenda())

    venda.finalizaVenda()

    # recupera as vendas para a data atual
    dtIni = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    dtFim = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    print(venda.getlistaVendas(xmlrpc.client.DateTime(dtIni), xmlrpc.client.DateTime(dtFim)))
