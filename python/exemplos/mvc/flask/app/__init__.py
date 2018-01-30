from flask import Flask, render_template, redirect, url_for, request, \
    jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from app.forms.produto import ProdutoForm

app = Flask("MVCFlask", template_folder='app/templates',
        static_folder='app/statics')

# Associa o script de configuração
app.config.from_object('config')

db = SQLAlchemy(app)

# Roteamento
from app.model.model import Venda, venda_schema, Produto, produto_schema
from app.model.model import ItemVenda, itemVenda_schema
from datetime import datetime

@app.route('/')
def index():
    pc = Produto.query.count() # Quantidade de Produto no sistema
    vc = Venda.query.count() # Quantidade de Venda no sistema
    return render_template('index.html', num_prods=pc, num_vendas=vc,
        dat_hora_atualizacao=datetime.now().strftime('%a, %d de %B de %Y, %H:%M:%S'))

@app.route('/get_produto', methods=['POST'])
def getProduto():
    prod_id = int(request.data)
    #produto = db.session.query(Produto).filter_by(id=prod_id).all()
    produto = Produto.query.filter_by(id=prod_id).all()

    if produto:
        jsonStr = jsonify({'id': produto[0].id,
                           'nome': produto[0].nome,
                           'vr_custo': float(produto[0].vr_custo),
                           'vr_venda': float(produto[0].vr_venda)})
        return jsonStr
    else:
        return ''


@app.route('/produtos', methods=['GET', 'POST'])
def produtos():

    erro = None
    form = ProdutoForm(request.form)

    if request.method == 'POST' and form.validate():

        if not request.form['nome']:
            erro = 'O nome não pode ser vazio.'
        else:
            p = Produto(nome=request.form['nome'],
                        vrCusto=request.form['vr_custo'],
                        vrVenda=request.form['vr_venda'])
            db.session.add(p)
            db.session.commit()
            flash('O registro foi salvo com sucesso!')
            return redirect(url_for('produtos'))

    produtos = Produto.query.all()
    return render_template('produtos.html', form=form, produtos=produtos, erro=erro,
        dat_hora_atualizacao=datetime.now().strftime('%a, %d de %B de %Y, %H:%M:%S'))
