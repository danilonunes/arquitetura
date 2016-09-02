#!/usr/bin/env python3

# ************************************************
#              IFNMG - Campus Januária
#                       TADS
#              Arquitetura de Software
# ************************************************
# ***************** exercício 01 ***************** 
# ************************************************
# Faça um programa em Python (>= 3) onde exista
# uma classe Pessoa com os seguintes atributos:
#   - nome;
#   - sexo;
#   - data_nasc (import datetime).
# 
# Os dados para referentes aos atributos devem
# ser informados no momento da instancialização
# do objeto. Cada atributo deve ser representado
# por uma propriedade (RW).
#
# ***************** ************ ***************** 

import datetime

class Pessoa(object):
    def __init__(self, nome, sexo, dt_nasc):
        self.__nome = nome
        self.__sexo = sexo
        self.data_nasc = dt_nasc
    
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
        if not valor:
            raise Exception("O valor informado para o atributo data_nasc é inválido.")
        
        #verificando se a data informada é maior que a data atual
        if not (valor <= datetime.date.today()):
            m = "Uma data de nascimento futura não é aceitável.\nValor informado: {0}".format(valor.isoformat())
            raise Exception(m)
            
        self.__data_nasc = valor

p1 = Pessoa('Danilo Nunes', 'M', datetime.date(2983, 3, 20))
print(p1)
print(p1.nome, '\n', p1.sexo, '\n', p1.data_nasc)

