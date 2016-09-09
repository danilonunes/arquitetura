#!/usr/bin/env python3

'''
*************************************************
*              IFNMG - Campus Januária          *
*                       TADS                    *
*              Arquitetura de Software          *
*************************************************
O arquivo cadastro.py é um pequeno programa para
cadastros feito em Python 3.* com o objetivo de
exemplificar o como usamos OO e aspectos ligados
a arquitetura de sw.
'''

__project_name__ = 'IFNMG - Januária - TADS - Arquitetura de Software'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2016-09-09T16:29:29.0'

import datetime as dt
import constantes
import oo_modulo as cn #cn = classes de negócio

class CadastroController(object):
    '''
    CadastroController -> clase controladora para as ações de
    cadastro.
    '''
    def __init__(self):
        self.__ultimoIdPessoa = None
        self.__pessoas = {} # dicionário que armazena os obj Pessoa cadastrados

    def __novoIdentificadorPessoa(self):

        if self.__ultimoIdPessoa:
            self.__ultimoIdPessoa = self.__ultimoIdPessoa + 1
        else:
            self.__ultimoIdPessoa = 1

        return self.__ultimoIdPessoa

    def incluirPessoa(self, nome, sexo, dt_nasc, est_civil, id=None):

        p = cn.Pessoa(nome, sexo, dt_nasc, est_civil)

        if id:
            if id in self.__pessoas.keys():
                raise Exception('KeyError: o ID informado já existe.')

            self.__pessoas[id] = p
        else:
            self.__pessoas[self.__novoIdentificadorPessoa()] = p

    def excluirPessoa(self, id):

        if id not in self.__pessoas.keys():
            raise Exception('KeyError: o ID informado não existe.')

        del(self.__pessoas[id])

    def listarPessoas(self):
        return self.__pessoas

if __name__ == '__main__':

    tarq = CadastroController()
    tarq.incluirPessoa('Danilo Nunes',
        constantes.MASCULINO, dt.date(1983, 3, 20),
        constantes.CASADO)
    print(tarq.listarPessoas())
