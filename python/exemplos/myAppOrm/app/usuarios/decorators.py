
from functools import wraps
from flask import g, flash, redirect, url_for, request

# flask.g : é um objeto no Flask que possui a responsabilidade de armazenar e 
#     compartilhar dados através do tempo de execução de uma requisição
# *args : o * é utilizado para permitir que um parâmetro aceite um número não 
#     definido de argumentos para sua função (parecido com a keyword params no C#)
# **kwargs : Da mesma forma, ** permite lidar com argumentos nomeados que não 
#     foram previamente definidos (parecido com a keyword params+dictonary no C#)

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
    	if g.user is None:
    		flash('Você precisa estar autenticado no sistema para ter acesso a essa página.')
    		return redirect(url_for('usuarios.login', next=request.path))
    	return f(*args, **kwargs)
    return decorated_function