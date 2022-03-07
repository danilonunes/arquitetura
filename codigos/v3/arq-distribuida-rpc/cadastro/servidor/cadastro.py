from model import Cliente, Endereco
from db import addRegisters, saveSession, session, startDatabase
from datetime import datetime
import json

class CadastroCTRL(object):
    '''
        Controladora-fachada (facade controller) para o cadastro
    '''

    def addCliente(self, nome, dtNascimento, cpf, logradouro, num, 
        bairro, cidade, estado):
        dt_nascimento = datetime.strptime(str(dtNascimento), '%Y%m%dT%H:%M:%S')
        c = Cliente(nome=nome, dtNascimento=dt_nascimento, cpf=cpf)
        c.endereco = [Endereco(logradouro=logradouro, 
                               numero=num, 
                               bairro=bairro, 
                               cidade=cidade,
                               estado=estado, 
                               cliente_id=c.id)]
        addRegisters([c])
        saveSession()
        return c.id
    
    def _doGetCliente(self, id):
        c = session.query(Cliente).filter(Cliente.id==id).first()
        return c

    def getCliente(self, idCliente):
        c = self._doGetCliente(idCliente)
        
        if not c:
            return None
        else:
            aux = { 'id': c.id,
                    'nome': c.nome,
                    'cpf': c.cpf,
                    'dtNascimento': datetime.strftime(
                        c.dtNascimento, '%Y%m%dT%H:%M:%S'),
            }

            c_json = json.dumps(aux, indent=4)
            return c_json
    
    def getClientes(self):
        listaCliente = session.query(Cliente).all()
        dict_aux = {}
        for i in listaCliente:
            dict_aux[i.id] = { 
                'nome': i.nome,
                'cpf': i.cpf,
                'dtNascimento': datetime.strftime(
                    i.dtNascimento, '%Y%m%dT%H:%M:%S'),
            }

        c_json = json.dumps(dict_aux, indent=4)
        return c_json

    def getClientesPorNome(self, nome):
        c = session.query(Cliente).\
            filter(Cliente.nome.ilike('%'+ nome +'%')).all()
        dict_aux = {}
        for i in c:
            dict_aux[i.id] = { 
                'nome': i.nome,
                'cpf': i.cpf,
                'dtNascimento': datetime.strftime(
                    i.dtNascimento, '%Y%m%dT%H:%M:%S'),
            }

        c_json = json.dumps(dict_aux, indent=4)
        return c_json

    def delCliente(self, idCliente):
        c = self._doGetCliente(idCliente)
        
        if not c:
            msg_err = "O Cliente com ID {0} não foi encontrado.".format(idCliente)
            raise Exception(msg_err)
        
        session.delete(c)
        saveSession()
