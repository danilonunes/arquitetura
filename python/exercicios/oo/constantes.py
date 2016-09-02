#!/usr/bin/env python3

# *******************************************************************************
#                           IFNMG - Campus Januária
#                                     TADS
#                           Arquitetura de Software
# *******************************************************************************
# ********************************* exemplo 02 ********************************** 
# *******************************************************************************
# Módulo dedicado às constantes usadas no exercício 01
# *******************************************************************************

__project_name__ = 'IFNMG - Januária - TADS - Arquitetura de Software'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2016-09-02T17:30:07.0'

# --------------------- constantes ---------------------

# sexo
MASCULINO = 'M'
FEMININO = 'F'
OUTROS = 'O'
SEXO = {MASCULINO: 'Masculino',
        FEMININO: 'Feminino',
        OUTROS: 'Outros',
}

# estado civil (fonte: https://pt.wikipedia.org)
#   Solteiro(a) - quem nunca se casou, ou que teve o casamento anulado
#   Casado(a) - quem contraiu matrimônio, independente do regime de bens adotado
#   Divorciado(a) - após a homologação do divórcio pela justiça ou por uma 
#       escritura pública.
#   Viúvo(a) - pessoa cujo cônjuge faleceu.
#   Separado(a) - pessoa cujo vínculo jurídico do casamento existe, mas foi 
#       dissolvida por escritura pública ou decisão judicial a sociedade conjugal
#   Companheiro(a) - pessoa que vive em união estável tornada pública pela
#       inscrição no Registro Civil nos termos de Provimento CNJ 37/2014
SOLTEIRO = 0
CASADO = 1
DIVORCIADO = 2
VIUVO = 3
SEPARADO = 4
COMPANHEIRO = 5
ESTADO_CIVIL = {SOLTEIRO: 'Solteiro(a)',
                CASADO: 'Casado(a)',
                DIVORCIADO: 'Divorciado(a)',
                VIUVO: 'Viúvo(a)',
                SEPARADO: 'Separado(a)',
                COMPANHEIRO: 'Companheiro(a)',
}

# fim --------------------- constantes ---------------------
