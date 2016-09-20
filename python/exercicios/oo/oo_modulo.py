#!/usr/bin/env python3

'''
    Esse módulo tem como objetivo apresentar a modularização das constantes.
    Para isso foi criado um arquivo chamado constantes.py
'''

# ************************************************
#              IFNMG - Campus Januária
#                       TADS
#              Arquitetura de Software
# ************************************************
#
# -------------------- constantes -------------------
# as constantes estão definidas em um módulo
# próprio chamado de constantes.py

import datetime
from constantes import MASCULINO, FEMININO, OUTROS, SEXO, ESTADO_CIVIL, SOLTEIRO
from constantes import CASADO, DIVORCIADO, VIUVO, SEPARADO, COMPANHEIRO

class Pessoa(object):
    '''
        Classe Pessoa para um simples cadastro
    '''
    def __init__(self, nome, sexo, dt_nasc, est_civil):
        self.nome = nome
        self.sexo = sexo
        self.data_nasc = dt_nasc
        self.estadoCivil = est_civil

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not valor or (valor == ''):
            raise Exception("O valor informado para o atributo nome é inválido.")
        self.__nome = valor

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, valor):
        if (not valor or (valor == '')
            or (valor not in ['F',
                'f', 'M', 'm', 'O', 'o'])):
            raise Exception("O valor informado para o atributo sexo é inválido.")
        self.__sexo = valor

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, valor):
        if not valor or not isinstance(valor, datetime.date):
            raise Exception("O valor informado para o atributo data_nasc é inválido.")

        #verificando se a data informada é maior que a data atual
        if not (valor <= datetime.date.today()):
            m = "Uma data de nascimento futura não é aceitável.\nValor informado: {0}".format(valor.isoformat())
            raise Exception(m)

        self.__data_nasc = valor


    @property
    def estadoCivil(self):
        return self.__est_civil

    @estadoCivil.setter
    def estadoCivil(self, valor):
        if not valor or (valor not in ESTADO_CIVIL.keys()):
            raise Exception("O valor informado para o atributo estadoCivil é inválido.")
        self.__est_civil = valor



# !!!!!!!!!!!!!!!! Testando... !!!!!!!!!!!!!!!!!!!
if __name__ == '__main__':

    p1 = Pessoa('Danilo Nunes',
                MASCULINO,
                datetime.date(1983, 3, 20),
                CASADO)

    print(p1.nome, '\n', SEXO[p1.sexo], '\n', p1.data_nasc, '\n',
        ESTADO_CIVIL[p1.estadoCivil])
    print('Modelo de objetos')
    print(p1.nome, '\n', p1.sexo, '\n', p1.data_nasc, '\n',
        p1.estadoCivil)
