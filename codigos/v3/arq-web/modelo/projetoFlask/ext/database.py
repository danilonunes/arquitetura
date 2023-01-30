from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)

class TypeProduct(db.Model, SerializerMixin):
    __tablename__ = "type_product"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150))

class Product(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)
    type_id = db.Column(db.Integer, db.ForeignKey('type_product.id'),
        nullable=False)
    type = db.relationship('TypeProduct', lazy=True)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))