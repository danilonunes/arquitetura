from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("MVCFlask", template_folder='app/templates')

# Associa o script de configuração
app.config.from_object('config')

db = SQLAlchemy(app)

# Roteamento
@app.route('/')
def index():
    return render_template('index.html', msg="Olha o Flask rodando")
