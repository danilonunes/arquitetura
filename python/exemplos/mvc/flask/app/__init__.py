from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("MVCFlask", template_folder='app/templates')

# Associa o script de configuração
app.config.from_object('config')

db = SQLAlchemy(app)

# Roteamento
from app.model.model import Venda, Produto, ItemVenda
from datetime import datetime

@app.route('/')
def index():
    pc = Produto.query.count()
    vc = Venda.query.count()
    return render_template('index.html', num_prods=pc, num_vendas=vc,
        dat_hora_atualizacao=datetime.now())

@app.route('/produtos')
def frmProduto():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos,
        dat_hora_atualizacao=datetime.now())
