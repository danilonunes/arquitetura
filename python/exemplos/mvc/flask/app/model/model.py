from app import db

class Produto(db.Model):
    __table_args__ = {'extend_existing': True}  # adicionado devido a bugs

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    vr_custo = db.Column(db.Float, nullable=False)
    vr_venda = db.Column(db.Float, nullable=False)

    def __init__(self, nome, vrCusto, vrVenda):
        self.nome = nome
        self.vr_custo = vrCusto
        self.vr_venda = vrVenda

    def __repr__(self):
        return '<Produto %r, %r, %r, %r>' % (self.id, self.nome, self.vr_custo, self.vr_venda)


class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itens = db.relationship('ItemVenda')

    @property
    def total(self):
        t = 0
        for i in self.itens:
            t += i.quantidade * i.valor

        return t

    def __repr__(self):
        return '<Venda %r, %r, %r>' % (self.id, self.itens, self.total)

class ItemVenda(db.Model):
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'),
                primary_key=True)
    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'),
                primary_key=True)

    produto = db.relationship('Produto', uselist=False)
    venda = db.relationship('Venda', uselist=False)
    quantidade = db.Column(db.Float, nullable=False)
    valor = db.Column(db.Float, nullable=False)

    def __init__(self, produto, qtde, vrVenda):
        self.produto = produto
        self.quantidade = qtde
        self.valor = vrVenda

    def __repr__(self):
        return '<ItemVenda %r, %r, %r, %r>' % (self.produto_id, self.venda_id,
            self.quantidade, self.valor)
