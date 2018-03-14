"""
###########################################################
##                                                       ##
##                IFNMG Campus Januária                  ##
##            Projeto Bate-papo Tecnológico              ##
##              Python Orientado a Objetos               ##
##          Exemplo de estrutura de uma classe           ##
##                  Prof. Danilo Nunes                   ##
##              <danilo.nunes@ifnmg.edu.br>              ##
###########################################################
"""

__project_name__ = 'Projeto Bate-papo Tecnológico'
__course_name__ = 'Python Orientado a Objetos'
__lesson__ = 'Estrutura de uma classe em Python'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__source__ = 'http://github.com/danilonunes/cursos'

# definindo a estrutura de uma classe Pessoa
class Pessoa(object):
    """
        Classe Pessoa definida para servir de exemplo do paradigma OO em
        Python 3.
    """

    def __init__(self):
        """
            Método de inicialização da intância de Pessoa:
             - Explicita os atributos existentes na classe.
        """
        # atributos 'protegidos'
        self._id = None
        self._nome = None
        self._sexo = None
        self._cpf = None

    @property
    def nome(self):
        """
            Propriedade (rw) nome: nome de uma pessoa
        """
        return self._nome

    @nome.setter
    def nome(self, value):
        if len(value) == 0:
            raise Exception('O nome \'{0}\' informado é inválido.'.format(value))

        self._nome = value

    @property
    def sexo(self):
        """
            Propriedade (rw) sexo : indica o sexo de uma pessoa - masculino, feminino e
                transgênero;
        """
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        if not (value in ['M', 'm', 'F', 'f', 'T', 't']):
            raise Exception('O sexo \'{0}\' informado é inválido.'.format(value))

        self._sexo = value

    @property
    def cpf(self):
        """
            Propriedade (rw) cpf: documento de identificação no Cadastro de
             Pessoa Física;
        """
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        if len(value) < 11:
            raise Exception('O CPF \'{0}\' informado é inválido.'.format(value))

        self._cpf = value

    @property
    def id(self):
        """
            Propriedade (r) id: apresenta o identificador (único) de uma pessoa.
        """
        # caso não tenha sido definido o ID retorna -1
        if not self._id:
            return -1
        else:
            return self._id

    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return '<Pessoa: %s, %s, %s, %d>' % (self.nome, self.cpf,
            self.sexo, self.id)

# verifica se o arquivo está sendo executado como programa ou importado como módulo
if __name__ == '__main__':

    p1 = Pessoa()

    # print(p1.__doc__) # pode ser usado mas a função help é mais completa
    help(p1) # pressione "q" para saír da documentação

    print(p1)
    p1.sexo = 'M'
    p1.cpf = '12345678901'
    print(p1)
