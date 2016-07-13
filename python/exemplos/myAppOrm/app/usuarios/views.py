# third party imports
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from datetime import datetime
from sqlalchemy.sql import or_


# local application imports
from app import db
from app.usuarios.forms import CadastroForm, LoginForm
from app.usuarios.models import Usuario
from app.usuarios.requests import app_before_request
from app.usuarios.decorators import requires_login
from app.usuarios.constants import SESSION_NAME_USER_ID



# validate_on_submit : função do WTForm, no qual verifica se o formulário é 
#     valido durante uma requisição do tipo POST ou PUT

# render_template : retorna um documento renderizado, no nosso caso todos html, 
#     de acordo com o arquivo template e o formulário passado

# flash : possibilita que mensagens declaradas na view sejam recuperadas no 
#     template e exibidas para o usuário

# @mod.route('/login/', methods=['GET', 'POST'])  : associa uma rota a uma 
#     função que estiver após sua definição. O primeiro parâmetro define por qual caminho será executado e o segundo parâmetro quais os métodos REST serão aceitos por essa rota.

mod = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@mod.before_request
def before_request():
	app_before_request()


@mod.route('/')
@mod.route('/me/')
@requires_login
def index():
	return render_template('usuarios/perfil.html', user=g.user)


@mod.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)

	# make sure data are valid, but doesn't validate password is right
	if form.validate_on_submit():

		usuario = Usuario.query.filter_by(nome_usuario=form.usuario.data).first()

		# we use werzeug to validate user's password
		if usuario and check_password_hash(usuario.senha, form.senha.data):

			# the session can't be modified as it's signed,
			# it's a safe place to store the user id
			session[SESSION_NAME_USER_ID] = usuario.id

			flash('Bem-vindo {0}'.format(usuario.nome_completo))
			return redirect(url_for('usuarios.index'))

		flash('Usuário ou senha incorretos', 'error-message')

	return render_template( 'usuarios/login.html', form=form)


@mod.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():
	form = CadastroForm(request.form)

	if form.validate_on_submit():

		usuarioCadastrado = Usuario.query.filter(or_(Usuario.nome_usuario == form.usuario.data,
							Usuario.email == form.email.data)).first()

		if usuarioCadastrado is not None:
			flash('Email ou usuário já cadastrados')
			return render_template('usuarios/cadastro.html', form=form)


		# create an user instance not yet stored in the database
		usuario = Usuario.NovoUsuarioParaCadastro(form.nome_completo.data, form.usuario.data, form.email.data,
						generate_password_hash(form.senha.data))

		# insert the record in our database and commit it
		db.session.add(usuario)

		db.session.commit()

		# log the user in, as he now has an id
		session[SESSION_NAME_USER_ID] = usuario.id

		# flash will display a message to the user
		flash('Cadastro efetuado com sucesso')

		# redirect user to the 'index' method of the user module
		return redirect(url_for('usuarios.index'))
		
	return render_template('usuarios/cadastro.html', form=form)


@mod.route('/logout/', methods=['GET'])
def logout():
    # remove the username from the session if it's there
    session.pop(SESSION_NAME_USER_ID, None)
    
    # redirect user to the 'index' method of the user module
    return redirect(url_for('usuarios.login'))