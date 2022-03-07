from rpc_server import ServerRPC
from twisted.web import server
from twisted.internet import reactor, endpoints

porta = 7080
print("Iniciando servidor na porta {0}...".format(porta))
cadastro = ServerRPC(allowNone=True)
endpoint = endpoints.TCP4ServerEndpoint(reactor, porta)
endpoint.listen(server.Site(cadastro))
reactor.run()