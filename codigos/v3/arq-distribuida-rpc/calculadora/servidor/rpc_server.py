from twisted.web import xmlrpc

class Calculadora(xmlrpc.XMLRPC):
    def xmlrpc_somar2numeros(self, x, y):
        return x + y
    
    def xmlrpc_subtrair2numeros(self, x, y):
        return x - y
    
    def xmlrpc_multiplicar2numeros(self, x, y):
        return x * y

    def xmlrpc_dividir2numeros(self, x, y):
        return x / y

