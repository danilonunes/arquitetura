'''
    _basedir : mantém o caminho de onde os scripts são executados
    DEBUG : utilizado como True em ambientes de desenvolvimento, permite que 
        eja exibido detalhadamente a requisição, caso ocorra algum erro durante 
        o processo
    SECRET_KEY : utilizado na criação dos cookies
    ADMINS : email do Administrador responsável pelo site
    SQLALCHEMY_DATABASE_URI e DATABASE_CONNECT_OPTIONS : opções de conexão do 
        SQLAlchemy
    CSRF_ENABLED e CSRF_SESSION_KEY : proteção contra fraude de posts
'''

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['danilo.nunes@gmail.com'])
SECRET_KEY = 'SECRET_KEY_FOR_SESSION_SIGNING'

# Define the path of our database inside the root application,
# where 'app.db' is the database's name
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTION = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'SOMETHING_IMPOSSIBLE_TO_GUEES'
