import click
from projetoFlask.ext.database import db
from projetoFlask.ext.auth import create_user
from projetoFlask.ext.database import Product


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Product(
            id=1, 
            name="Produto 1", 
            price="10.00", 
            description="Produto 1 para teste"),
        Product(
            id=2, 
            name="Produto 2", 
            price="20.00", 
            description="Produto 2 para teste"),
        Product(
            id=3, 
            name="Produto 3", 
            price="30.00", 
            description="Produto 3 para teste"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)