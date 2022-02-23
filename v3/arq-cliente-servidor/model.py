from this import d
import db
from sqlalchemy import Column, Integer, String, DateTime

class Cliente(db.Base):

    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String)
    dtNascimento = Column(DateTime, nullable=False)



    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return '<Cliente: %s, %s, %s, %d>' % (self.nome, self.cpf,
            self.dtNascimento, self.id)