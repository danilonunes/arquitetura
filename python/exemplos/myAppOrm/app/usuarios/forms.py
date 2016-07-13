from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, EqualTo, Email


class LoginForm(Form):
	usuario = TextField('Usuário', [Required()])
	senha = PasswordField('Senha', [Required()])


class CadastroForm(Form):
	nome_completo = TextField('Nome Completo', [Required()])
	usuario = TextField('Nome de usuário', [Required()])
	email = EmailField('Email', [Email(), Required()])
	senha = PasswordField('Senha', [Required()])
	confirmacao = PasswordField('Repetição da senha', [
		Required(),
		EqualTo('senha', message='As senhas devem ser iguais')
])