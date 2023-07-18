from dynaconf import FlaskDynaconf
from flask import Flask, render_template
from views import produto
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#def create_app(self, app):
#    app = Flask(__name__)
#    return app

app = Flask(__name__)
FlaskDynaconf(app, load_dotenv=True)
Bootstrap(app)
db = SQLAlchemy(app)

# comandos que são executados mais de uma vez
@app.cli.command()
def createdb():
    """criando o database"""
    db.create_all()
