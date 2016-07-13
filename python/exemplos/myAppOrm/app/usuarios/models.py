# third party imports
from sqlalchemy.sql import extract, func

# local application imports
from app import db
from app.usuarios import constants as USUARIO


class Usuario(db.Model):
    # Map model to db table
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), unique=True)
    nome_usuario = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    senha = db.Column(db.String(20))
    regra = db.Column(db.SmallInteger, default=USUARIO.OPERADOR)
    situacao = db.Column(db.SmallInteger, default=USUARIO.NOVO)

    
    # Class Constructor
    def __init__(self, id=None):
    	self.id = id


    # Factory Constructor of a new user to register
    @classmethod
    def NovoUsuarioParaCadastro(cls, nome=None, nome_usuario=None, email=None, senha=None):
    	_usuario = cls()
    	_usuario.nome_completo = nome
    	_usuario.nome_usuario = nome_usuario
    	_usuario.email = email
    	_usuario.senha = senha
    	return _usuario
    
    
    
    def getSituacao(self):
    	return USUARIO.SITUACAO[self.situacao]
    
    
    def getRegra(self):
    	return USUARIO.REGRA[self.regra]


    def __repr__(self):
        return '<User %r><user   %r>' % (self.name)