from datetime import datetime
import db
from sqlalchemy import Column, Integer, String, DateTime, \
    ForeignKey, Float, select, func
from sqlalchemy.orm import relationship, column_property

class Cliente(db.Base):

    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    dtNascimento = Column(DateTime, nullable=False)
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now)
    endereco = relationship("Endereco", cascade="all, delete",
                            passive_deletes=True)

    compras = relationship("Venda")


    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return '<Cliente: %s, %s, %s, %d, %s, %s, %s>' % (self.nome, 
                self.cpf, self.dtNascimento, self.id, self.endereco,
                self.compras, self.dt_hr_manutencao)


class Endereco(db.Base):

    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    logradouro = Column(String, nullable=False)
    numero = Column(String)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cliente_id = Column(Integer, 
                        ForeignKey("cliente.id", 
                                    ondelete="CASCADE"),
                        )
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now)

    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return '<Endereco: %s, %s, %s, %s, %s, %d, %d, %s>' % (
            self.logradouro, self.numero, self.bairro, 
            self.cidade, self.estado, self.id, self.cliente_id,
            self.dt_hr_manutencao)

class Produto(db.Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False) 
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now) 

    def __repr__(self):
        return "<Produto: {0}, {1}, {2}>".format(self.id, 
                   self.descricao, self.dt_hr_manutencao)

class ItemVenda(db.Base):
    __tablename__ = "item_venda"
    venda_id = Column(Integer, ForeignKey("venda.id"), primary_key=True)
    produto_id = Column(Integer, ForeignKey("produto.id"), primary_key=True)
    produto = relationship("Produto")
    quantidade = Column(Float, default=0.00, nullable=False)
    valor = Column(Float, default=0.00, nullable=False)
    subtotal = column_property(quantidade * valor)
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now) 

    def __repr__(self):
        return "<ItemVenda: {}, {}, {}, {}, {}>".format(self.venda_id,
                 self.produto_id, self.quantidade, self.valor,
                 self.dt_hr_manutencao)

class Venda(db.Base):
    __tablename__ = "venda"
    id = Column(Integer, primary_key=True)
    dt_venda = Column(DateTime, nullable=False)
    cliente_id = Column(Integer, ForeignKey(Cliente.id), nullable=False)
    estado = Column(String(1), nullable=False, default='i')
    itens = relationship("ItemVenda")
    valor_total = column_property(
        select(func.sum(ItemVenda.subtotal))
        .where(ItemVenda.venda_id==id)
        .correlate_except(ItemVenda)
        .scalar_subquery()
    )
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now) 
    def __repr__(self):
        return "<Venda: {0}, {1}, {2}, {3}, {4}>".format(self.id,
                   self.dt_venda, self.cliente_id, self.itens,
                   self.dt_hr_manutencao)
