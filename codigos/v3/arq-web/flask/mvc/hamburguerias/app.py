from flask import Flask
from flask_bootstrap import Bootstrap
from hamburguerias.ext import authentication, database, configuration, admin,\
    commands
from hamburguerias import model
from hamburguerias import view

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    view.init_app(app)
    authentication.init_app(app)
    admin.init_app(app)
    return app
