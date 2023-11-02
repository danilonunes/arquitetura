from model import Cliente, Endereco, Produto, Venda, ItemVenda
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

    def addProduto(self, descricao):
        p = Produto(descricao=descricao)
        addRegisters([p])
        saveSession()

        return p.id

    def getProdutos(self):
        lp = session.query(Produto).all()

        dict_aux = {}
        for p in lp:
            dict_aux[p.id] = {
                'descricao': p.descricao,
            }

        p_json = json.dumps(dict_aux, indent=4)
        
        return p_json

    def _doGetProduto(self, id):
        p = session.query(Produto).filter(Produto.id==id).first()
        if not p:
            raise Exception("Produto {} não encontrado".format(id)) 

        return p

    def GetProduto(self, idProduto):
        p = self._doGeProduto
        d = {}
        d[p.id] = {
            "descricao": p.descricao,
        }

        return json.dumps(d, indent=4)

    def iniciarVenda(self, idCliente):
        v = Venda(cliente_id=idCliente, 
                  dt_venda= datetime.today().date(),
                  estado='i')
        addRegisters([v])
        saveSession()
        return v.id

    def _doGetVenda(self, idVenda):
        v = session.query(Venda).filter(Venda.id==idVenda).first()
        if not v:
            raise Exception("Venda {} não encontrada.".format(idVenda))

        return v

    def addItemVenda(self, idVenda, idProduto, quantidade, valor):
        v = self._doGetVenda(idVenda)
        p = self._doGetProduto(idProduto)
        iv = ItemVenda(venda_id=v.id, produto_id=p.id, 
                       quantidade=quantidade, valor=valor)
        addRegisters([iv])
        saveSession()

    def getValorTotalVenda(self, idVenda):
        v = self._doGetVenda(idVenda)
        d = {"valor": v.valor_total}

        return json.dumps(d, indent=4)

    def finalizarVenda(self, idVenda):
        v = self._doGetVenda(idVenda)
        v.estado = 'f'
        addRegisters([v])
        saveSession()
