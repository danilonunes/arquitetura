from xmlrpc.server import SimpleXMLRPCServer

PORT = 8384
server = SimpleXMLRPCServer(("localhost", PORT))

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

server.register_function(somar, "somar")
server.register_function(subtrair, "subtrair")
server.register_function(multiplicar, "multiplicar")
server.register_function(dividir, "dividir")

print("Servidor de aplicação XMLRPC MVC na porta {0}".format(PORT))
server.serve_forever()
