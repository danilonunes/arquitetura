from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


# Basic Routes #

@app.route('/')
def index():
	return redirect(url_for('usuarios.index'))

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404


# BluePrints - Modules #
# Blueprint basicamente permite que um módulo estenda a aplicação principal e 
# funcione similarmente a aplicação Flask. Sendo esta uma das grandes vantagem 
# para aplicações maiores, por permitir a modularização de uma aplicação, o que 
# facilita em muito a organização, desenvolvimento e manutenções do código fonte.

# Users Module
from app.usuarios.views import mod as usersModule
app.register_blueprint(usersModule)
