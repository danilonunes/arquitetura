import xmlrpc.client
PORT = 8384

calculadora = xmlrpc.client.ServerProxy("http://localhost:{0}/".format(PORT))

x = 1
y = 5
print("{0} + {1} = {2}".format(x, y, calculadora.somar(x, y)))
print("{0} - {1} = {2}".format(x, y, calculadora.subtrair(x, y)))
print("{0} * {1} = {2}".format(x, y, calculadora.multiplicar(x, y)))
print("{0} / {1} = {2}".format(x, y, calculadora.dividir(x, y)))
