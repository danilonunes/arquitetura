#!/usr/bin/env python3

'''
    IFNMG campus Januária
    Disciplina: Arquitetura de Software
    Autor: Danilo Nunes
    Assunto: Orientação a Objetos
    Exercício: controle de estoque
    Última atualização: 19/04/2016

'''

import datetime

class ControleEstoqueController():

    def __init__(self):
        self.__produtos = {}
        self.__unidades_medida = {}
        self.__categorias_produto = {}
        self.__next_cat_prod_id = 1 # próximo ID para Categoria de Produto
        self.__next_prod_id = 1 # próximo ID para Produto

    def __incrementaProxIdCategoriaProduto(self):
        self.__next_cat_prod_id = self.__next_cat_prod_id + 1
        
    def __incrementaProxIdProduto(self):
        self.__next_prod_id = self.__next_prod_id + 1
        
    # métodos para manipulação de objetos UnidadeMedida
    def incluirUnidadeMedida(self, pNome, pSigla):
        if pSigla in self.__unidades_medida:
            raise Exception('Já existe uma Unidade de Medida identificada pela sigla ', pSigla, '.')

        um = UnidadeMedida()
        um.nome = pNome
        um.sigla = pSigla
        self.__unidades_medida[pSigla] = um


    def excluirUnidadeMedida(self, pSigla):
        if not pSigla in self.__unidades_medida:
            raise Exception('Unidade de Medida \'', pSigla, '\' não encontrada.')

        del self.__unidades_medida[pSigla]

    def alterarUnidadeMedida(self, pSigla, pNome):
        if pSigla in self.__unidades_medida:
            if self.__unidades_medida[pSigla] != pNome:
                self.__unidades_medida[pSigla] = pNome
        else:
            raise Exception('Unidade de Medida com SIGLA \'', pSigla, '\' não encontrada.')

    def getListaUnidadeMedida(self):
        '''
            Método que retorna uma lista onde cada item representa um objeto
            UnidadeMedida em forma de tupla.
                Ex.:
                        ums = getListaUnidadeMedida()
                        if not len(ums) == 0: # verifica se não é vazio
                            print('Sigla: ', ums[0][0], ' Nome: ', ums[0][1])
        '''

        t = [] # instanciando uma lista
        for i in self.__unidades_medida.items():
            t.append((i[0], i[1].nome)) # adiciona uma tupla dentro da lista t
        return t

    def __getUnidadeMedida(self, pSigla):
        if pSigla in self.__unidades_medida:
            return self.__unidades_medida[pSigla]
        else:
            raise Exception('Unidade de Medida com SIGLA \'', pSigla, '\' não encontrada.')
            
    # fim *** métodos para manipulação de objetos UnidadeMedida

    # métodos para manipulação de objetos CategoriaProduto
    def incluirCategoriaProduto(self, pNome, pDescricao):
        cp = CategoriaProduto()
        cp.nome = pNome
        cp.descricao = pDescricao
        cp.id = self.__next_cat_prod_id
        self.__incrementaProxIdCategoriaProduto()
        self.__categorias_produto[cp.id] = cp
        
        
    def excluirCategoriaProduto(self, pId):
        if not pId in self.__categorias_produto:
            raise Exception('Categoria de produto com ID \'', pId, '\' não encontrada.')

        del self.__categorias_produto[pId]
        

    def alterarCategoriaProduto(self, pId, pNome, pDescricao):
        if pId in self.__categorias_produto:
            if (not pNome is None) or (self.__categorias_produto[pId].nome != pNome):
                self.__categorias_produto[pId].nome = pNome
            if (not pDescricao is None) or (self.__categorias_produto[pId].descricao != pDescricao):
                self.__categorias_produto[pId].descricao = pDescricao
        else:
            raise Exception('Categoria de produto com ID \'', pId, '\' não encontrada.')
    
    
    def getListaCategoriaProduto(self):
        '''
            Método que retorna uma lista onde cada item representa um objeto
            CategoriaProduto em forma de tupla.
                Ex.:
                        cps = getListaCategoriaProduto()
                        if not len(cps) == 0: # verifica se não é vazio
                            print('ID: ', cps[0], ' Nome: ', cps[1], ' Descrição: ', cps[2])
        '''

        t = [] # instanciando uma lista
        for i in self.__categorias_produto.items():
            t.append((i[0], i[1].nome, i[1].descricao)) # adiciona uma tupla dentro da lista t
        return t

    def __getCategoriaProduto(self, pId):
        if pId in self.__categorias_produto:
            return self.__categorias_produto[pId]
        else:
            raise Exception('Categoria de produto com ID \'', pId, '\' não encontrada.')
            
    # fim *** métodos para manipulação de objetos CategoriaProduto

    # métodos para manipulação de objetos Produto
    def incluirProduto(self, pNome, pIdCategoria, pSiglaUniMedida, pQtde, pQtdeMin=0, pQtdeMax=0, pVrCusto=0, pVrMinVenda=0, pVrMaxVenda=0):
        p = Produto()
        p.nome = pNome
        p.qtde_minima = pQtdeMin
        p.qtde_maxima = pQtdeMax
        p.quantidade = pQtde
        p.vr_custo = pVrCusto
        p.vr_min_venda = pVrMinVenda
        p.vr_max_venda = pVrMaxVenda
        p.id = self.__next_prod_id
        p.categoria = self.__getCategoriaProduto(pIdCategoria)
        p.unidade_medida = self.__getUnidadeMedida(pSiglaUniMedida)
        self.__produtos[p.id] = p
        self.__incrementaProxIdProduto()

    def excluirProduto(self, pId):
        if not pId in self.__produtos:
            raise Exception('Produto com ID \'', pId, '\' não encontrado.')

        del self.__produtos[pId]

    def alterarProduto(self, pId, pNome, pQtde, pQtdeMin, pQtdeMax, pVrCusto, pIdCategoria, pSiglaUniMedida, pVrMinVenda, pVrMaxVenda):
        if pId in self.__produtos:
            if self.__produtos[pId].nome != pNome:
                self.__produtos[pId].nome = pNome
                
            if self.__produtos[pId].qtde != pQtde:
                self.__produtos[pId].qtde = pQtde
                
            if self.__produtos[pId].qtde_minima != pQtdeMin:
                self.__produtos[pId].qtde_minima = pQtdeMin
                
            if self.__produtos[pId].qtde_maxima != pQtdeMax:
                self.__produtos[pId].qtde_maxima = pQtdeMax
                
            if self.__produtos[pId].vr_custo != pVrCusto:
                self.__produtos[pId].vr_custo = pVrCusto
                
            if self.__produtos[pId].vr_min_venda != pVrMinVenda:
                self.__produtos[pId].vr_min_venda = pVrMinVenda
                
            if self.__produtos[pId].vr_max_venda != pVrMaxVenda:
                self.__produtos[pId].vr_max_venda = pVrMaxVenda
            
            if self.__produtos[pId].categoria.id != pIdCategoria:
                self.__produtos[pId].categoria = self.__getCategoriaProduto(pIdCategoria)
                
            if self.__produtos[pId].unidade_medida.sigla != pSiglaUniMedida:
                self.__produtos[pId].unidade_medida = self.__getUnidadeMedida(pSiglaUniMedida)

        else:
            raise Exception('Produto com ID \'', pId, '\' não encontrado.')

    def getListaProduto(self):
        '''
         ;-)
        '''

        t = [] # instanciando uma lista
        for i in self.__produtos.items():
            t.append((i[0], i[1].nome, i[1].quantidade, i[1].qtde_minima, 
                i[1].qtde_maxima, i[1].vr_custo, i[1].vr_min_venda, 
                i[1].vr_max_venda, i[1].dt_inclusao, i[1].categoria.id, 
                i[1].unidade_medida.sigla)) # adiciona uma tupla dentro da lista t
        return t

    # fim *** métodos para manipulação de objetos Produto

class UnidadeMedida:
    def __init__(self):
        self.__nome = ''
        self.__sigla = ''
        self.__dt_inclusao = datetime.datetime.now()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value=''):
        if value == '':
            raise Exception('O atributo NOME não pode ser vazio.')
        self.__nome = str(value)

    @property
    def sigla(self):
        return self.__sigla

    @sigla.setter
    def sigla(self, value=''):
        if value == '':
            raise Exception('O atributo SIGLA não pode ser vazio.')
        self.__sigla = str(value)

class CategoriaProduto:
    def __init__(self):
        self.__id = None
        self.__nome = ''
        self.__descricao = ''
        self.__dt_inclusao = datetime.datetime.now()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = str(value)

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = str(value)

class Produto:
    def __init__(self):
        # definindo atributos
        self.__id = None
        self.__nome = ''
        self.__qtde = 0
        self.__qtde_min = 0
        self.__qtde_max = 0
        self.__vr_custo = 0
        self.__vr_min_venda = 0
        self.__vr_max_venda = 0
        self.__categoria = None
        self.__unidade_medida = None
        self.__dt_inclusao = datetime.datetime.now()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def quantidade(self):
        return self.__qtde

    @quantidade.setter
    def quantidade(self, value):
        if (value < self.__qtde_min) or (value > self.__qtde_max):
            raise Exception('A quantidade informada diverge da parametrização atual:\n\t',
            'quantidade mínima: ', self.__qtde_min, '\n\tquantidade máxima: ', self.__qtde_max)
            
        self.__qtde = value

    @property
    def qtde_minima(self):
        return self.__qtde_min

    @qtde_minima.setter
    def qtde_minima(self, value):
        self.__qtde_min = value if value > 0 else 0

    @property
    def qtde_maxima(self):
        return self.__qtde_max

    @qtde_maxima.setter
    def qtde_maxima(self, value):
        self.__qtde_max = value if value > 0 else 0

    @property
    def vr_custo(self):
        return self.__vr_custo

    @vr_custo.setter
    def vr_custo(self, value):
        self.__vr_custo = value if value > 0 else 0

    @property
    def vr_min_venda(self):
        return self.__vr_min_venda

    @vr_min_venda.setter
    def vr_min_venda(self, value):
        self.__vr_min_venda = value if value > 0 else 0

    @property
    def vr_max_venda(self):
        return self.__vr_max_venda

    @vr_max_venda.setter
    def vr_max_venda(self, value):
        self.__vr_max_venda = value if value > 0 else 0

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, value):
        if isinstance(value, CategoriaProduto):
            self.__categoria = value
        else:
            raise Exception('O objeto informado não é do tipo \'CategoriaProduto\'')
            
    @property
    def unidade_medida(self):
        return self.__unidade_medida

    @unidade_medida.setter
    def unidade_medida(self, value):
        if isinstance(value, UnidadeMedida):
            self.__unidade_medida = value
        else:
            raise Exception('O objeto informado não é do tipo \'UnidadeMedida\'')

    @property
    def dt_inclusao(self):
        return self.__dt_inclusao

if __name__ == '__main__':
    tam_menu = 100
    menu = '-' * tam_menu
    menu_um = 'Unidades de Medida'
    menu_um_len = len(menu_um)
    menu_cp = 'Categorias de Produto'
    menu_cp_len = len(menu_cp)
    menu_prod = 'Produtos'
    menu_prod_len = len(menu_prod)
    
    def imprimeCabecalho(pTexto='', pTextoLen=0):
        print(menu)
        print('-' * int((tam_menu - pTextoLen) / 2), ' ' * 5, pTexto, 
          ' ' * 5, '-' * int((tam_menu - pTextoLen) / 2))
        print(menu)        
        
    ce = ControleEstoqueController()

    ce.incluirUnidadeMedida('quilo', 'kg')
    ce.incluirUnidadeMedida('peça', 'pc')
    ce.incluirUnidadeMedida('metro', 'm')
    ce.incluirUnidadeMedida('mililitros', 'ml')

    imprimeCabecalho(menu_um, menu_um_len)
    for i in sorted(ce.getListaUnidadeMedida()):
        print(i[0], ': ', i[1])
    print(menu)

    ce.incluirCategoriaProduto('Produtos relacionados a limpeza', 'Limpeza')
    ce.incluirCategoriaProduto('Produtos relacionados a alimentação humana', 
        'Alimentação humana')
    ce.incluirCategoriaProduto('Produtos relacionados a bebida alcoólica', 
        'Bebida alcoólica')
    ce.incluirCategoriaProduto('Produtos relacionados a alimentação de pets', 
        'Alimentação pets')

    imprimeCabecalho(menu_cp, menu_cp_len)
    for i in sorted(ce.getListaCategoriaProduto()):
        print(i[0], '-> ', i[1], ' -> ', i[2])
    print(menu)
    
    ## pNome, pIdCategoria, pSiglaUniMedida, pQtde, pQtdeMin=0, pQtdeMax=0, pVrCusto=0, pVrMinVenda=0, pVrMaxVenda=0
    ce.incluirProduto('Costela suína', 2, 'kg', 5, 1, 30, 8.00, 14.50, 17.50)
    ce.incluirProduto('Costela bovina', 2, 'kg', 5, 5, 100, 6.00, 12.50, 15.50)
    ce.incluirProduto('Ração Kynus', 4, 'kg', 200, 50, 500, 0.90, 1.80, 2.50)
    ce.incluirProduto('Pano de algodão alvejado', 1, 'm', 12, 5, 20, 8.00, 14.50, 17.50)

    imprimeCabecalho(menu_prod, menu_prod_len)
    for i in sorted(ce.getListaProduto()):
        print('|', i[0], ' | ', i[1], ' | ', i[2], ' | ', i[3], ' | ', i[4], ' | ',
                i[5], ' | ', i[6], ' | ', i[7], ' | ', i[8], ' | ', i[9], ' | ',
                i[10], ' |')
    print(menu)

#    while true:
#        print("Escolha uma das opções abaixo:")
#        print("1 -> Incluir nova Unidade de Medida")
#        print("2 -> Incluir nova Categoria de Produto")
#        print("1 -> Incluir novo Produto")
#        break
