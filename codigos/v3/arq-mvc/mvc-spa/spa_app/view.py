from app import create_app
from flask import render_template

def index(self):
    products = ['produto 1', 'produto 2']
    return render_template('index.html', product=product)

