import constants as const

class Endereco(object):
    '''
        Classe Endereço:
        Na instancialização de um ojeto dessa classe podemos informar os
        seguintes parâmetros:
            - logradouro (str)
            - numero (str)
            - complememto (str)
            - bairro (str)
            - cep (strs)
            - estado (str)
            - cidade (str)
            - pais (str)
    '''
    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            if 'logradouro' in kwargs:
                self.logradouro = kwargs['logradouro']

            if 'numero' in kwargs:
                self.numero = kwargs['numero']

            if 'complemento' in kwargs:
                self.complemento = kwargs['complemento']

            if 'bairro' in kwargs:
                self.bairro = kwargs['bairro']

            if 'cidade' in kwargs:
                self.cidade = kwargs['cidade']

            if 'pais' in kwargs:
                self.pais = kwargs['pais']

            if 'cep' in kwargs:
                self.cep = kwargs['cep']

            if 'estado' in kwargs:
                self.estado = kwargs['estado']

    # propriedades - gets ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def numero(self):
        return self.__numero

    @property
    def complemento(self):
        return self.__complemento

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade

    @property
    def pais(self):
        return self.__pais

    @property
    def cep(self):
        return self.__cep

    @property
    def estado(self):
        return self.__estado

    # propriedades - sets ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @logradouro.setter
    def logradouro(self, value):
        if isinstance(value, str) and (len(value) > 0):
            self.__logradouro = value
        else:
            raise ValueError(const.EMSG[const.LGRERROR])

    @numero.setter
    def numero(self, value):
        if isinstance(value, str) and (len(value) > 0):
            self.__numero = value
        else:
            raise ValueError(const.EMSG[const.NUMERROR])

    @complemento.setter
    def complemento(self, value):
        if isinstance(value, str) and (len(value) > 0):
            self.__complemento = value
        else:
            raise ValueError(const.EMSG[const.COMERROR])

    @bairro.setter
    def bairro(self, value):
        if isinstance(value, str):
            self.__bairro = value
        else:
            raise ValueError(const.EMSG[const.BAIERROR])

    @cidade.setter
    def cidade(self, value):
        if isinstance(value, str):
            self.__cidade = value
        else:
            raise ValueError(const.EMSG[const.CIDERROR])

    @pais.setter
    def pais(self, value):
        if isinstance(value, str):
            self.__pais = value
        else:
            raise ValueError(const.EMSG[const.PAISERROR])

    @cep.setter
    def cep(self, value):
        if isinstance(value, str):
            self.__cep = value
        else:
            raise ValueError(const.EMSG[const.CEPERROR])

    @estado.setter
    def estado(self, value):
        if isinstance(value, str):
            self.__estado = value
        else:
            raise ValueError(const.EMSG[const.ESTERROR])


class Telefone(object):
    '''
        Classe Telefone:
        Na instancialização de um ojeto dessa classe podemos informar os
        seguintes parâmetros:
            - codpais (str)
            - ddd (str)
            - numero (str)
            - ramal (str)
    '''
    def __init__(self, **kwargs):
        if len(kwargs) > 0:
            if 'codpais' in kwargs:
                self.cod_pais = kwargs['codpais']

            if 'ddd' in kwargs:
                self.ddd = kwargs['ddd']

            if 'numero' in kwargs:
                self.numero = kwargs['numero']

            if 'ramal' in kwargs:
                self.ramal = kwargs['ramal']

    # propriedades - gets ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def codpais(self):
        return self.__codpais

    @property
    def ddd(self):
        return self.__ddd

    @property
    def numero(self):
        return self.__numero

    @property
    def ramal(self):
        return self.__ramal

    # propriedades - sets ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @codpais.setter
    def codpais(self, value):
        if isinstance(value, str):
            self.__codpais = value
        else:
            raise ValueError(const.EMSG[const.PAISERROR])

    @ddd.setter
    def ddd(self, value):
        if isinstance(value, str):
            self.__ddd = value
        else:
            raise ValueError(const.EMSG[const.DDDERROR])

    @numero.setter
    def numero(self, value):
        if isinstance(value, str):
            self.__numero = value
        else:
            raise ValueError(const.EMSG[const.NUMERROR])

    @ramal.setter
    def ramal(self, value):
        if isinstance(value, str):
            self.__ramal = value
        else:
            raise ValueError(const.EMSG[const.RMLERROR])


if __name__ == "__main__":
    #print(Endereco.__doc__)
    #print(Telefone.__doc__)
    e1 = Endereco(logradouro='Fazenda São Geraldo',
                numero='s/n',
                complemento='Dir. Informática',
                bairro='Bom Jardim',
                cidade='Januária',
                estado='MG',
                cep='39480-000',
                pais='Brasil',)
    print(e1)

    t1 = Telefone(codpai='+55',
                ddd='38',
                numero='36294600',
                ramal='')
    print(t1)
