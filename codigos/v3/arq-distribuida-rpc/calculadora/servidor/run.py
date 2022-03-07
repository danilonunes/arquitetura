from rpc_server import Calculadora
from twisted.web import server
from twisted.internet import reactor, endpoints

porta = 7080
print("Iniciando servidor na porta {0}...".format(porta))
calculadora = Calculadora()
endpoint = endpoints.TCP4ServerEndpoint(reactor, porta)
endpoint.listen(server.Site(calculadora))
reactor.run()