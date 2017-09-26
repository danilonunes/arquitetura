# ************************************************
#              IFNMG - Campus Januária
#                       TADS
#              Arquitetura de Software
# ************************************************
#           Exemplo de herança em Python 3
# ***************** ************ *****************

from abc import ABC, abstractmethod
import validators
import constants as const
from classes_base import Endereco, Telefone

class Pessoa(ABC):
    def __init__(self, **kwargs):

        # verificando se foram passados parâmetros e argumentos
        if len(kwargs) > 0:
            if 'nome' in kwargs:
                self.nome = kwargs['nome']

            if 'endereco' in kwargs:
                self.endereco = kwargs['endereco']

            if 'telefone' in kwargs:
                self.telefone = kwargs['telefone']

            if 'email' in kwargs:
                self.email = kwargs['email']

            if 'site' in kwargs:
                self.site = kwargs['site']

            super(Pessoa, self).__init__()

    # propriedades - gets ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @property
    def site(self):
        return self.__site

    # propriedades - sets ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @nome.setter
    def nome(self, value):
        if isinstance(value, str):
            self.__nome = value
        else:
            raise ValueError(const.EMSG[const.NOMEERROR])

    @endereco.setter
    def endereco(self, value):
        if isinstance(value, Endereco):
            self.__endereco = value
        else:
            raise ValueError(const.EMSG[const.ENDERERROR])

    @telefone.setter
    def telefone(self, value):
        if isinstance(value, Telefone):
            self.__telefone = value
        else:
            raise ValueError(const.EMSG[const.TELERROR])

    @email.setter
    def email(self, value):
        if validators.email(value):
            self.__email = value
        else:
            raise ValueError(const.EMSG[const.EMAILERROR])

    @site.setter
    def site(self, value):
        if validators.url(value):
            self.__site = value
        else:
            raise ValueError(const.EMSG[const.URLERROR])

    @abstractmethod
    def _validaDocumentos(self, pDocumento, pTipo):
        """
            Método abstrado para validação de documento(s)
            existente(s) na(s) classe(s) herdeira(s)
        """
        pass


class PessoaFisica(Pessoa):
    """docstring for PessoaFisica"""
    def __init__(self, **kwargs):
        super(PessoaFisica, self).__init__(kwargs)

    def _validaDocumentos(self, pDocumento, pTipo):
        pass

class PessoaJuridica(Pessoa):
    """docstring for PessoaJuridica"""
    def __init__(self, **kwargs):
        super(PessoaJuridica, self).__init__(kwargs)

    def _validaDocumentos(self, pDocumento, pTipo):
        pass



if __name__ == "__main__":

    p = Pessoa(nome="Danilo Nunes")
    print(p)
