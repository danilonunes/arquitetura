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
            raise Exception('Unidade de Medida \'', pSigla, '\' não encontrada.')

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
            t.append((i[0], i[1].nome)) # adiciona uma tupla dentro da lista l
        return t

    # fim *** métodos para manipulação de objetos UnidadeMedida

    # métodos para manipulação de objetos CategoriaProduto
    def incluirCategoriaProduto(self):
        pass

    def excluirCategoriaProduto(self):
        pass

    def alterarCategoriaProduto(self):
        pass
    # fim *** métodos para manipulação de objetos CategoriaProduto

    # métodos para manipulação de objetos Produto
    def incluirProduto(self):
        pass

    def excluirProduto(self):
        pass

    def alterarProduto(self):
        pass
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
        self.__nome = ''
        self.__descricao = ''
        self.__dt_inclusao = datetime.datetime.now()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = srt(value)

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = srt(value)

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
        self.__qtde = value if value > 0 else 0

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

if __name__ == '__main__':
    ce = ControleEstoqueController()

    ce.incluirUnidadeMedida('quilo', 'kg')
    ce.incluirUnidadeMedida('peça', 'pc')
    ce.incluirUnidadeMedida('metro', 'm')
    ce.incluirUnidadeMedida('mililitros', 'ml')
    for i in sorted(ce.getListaUnidadeMedida()):
        print(i[0], ': ', i[1])


#    while true:
#        print("Escolha uma das opções abaixo:")
#        print("1 -> Incluir nova Unidade de Medida")
#        print("2 -> Incluir nova Categoria de Produto")
#        print("1 -> Incluir novo Produto")
#        break