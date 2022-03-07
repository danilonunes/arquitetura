import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:7080")

print("*" * 40)
print("\tCliente da Calculadora RPC")
print("*" * 40)

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))

soma = server.somar2numeros(a,b)
print("Soma: {0} + {1} = {2}".format(a, b, soma))

diferenca = server.subtrair2numeros(a,b)
print("Subtração: {0} - {1} = {2}".format(a, b, diferenca))

produto = server.multiplicar2numeros(a,b)
print("Multiplicação: {0} x {1} = {2}".format(a, b, produto))

quociente = server.dividir2numeros(a,b)
print("Divisão: {0} / {1} = {2}".format(a, b, quociente))
