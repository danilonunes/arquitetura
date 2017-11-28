from flask import Flask, render_template, redirect, url_for
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask("MVCFlask")
app.config.from_object('config')

#db = SQLAlchemy(app)

# Roteamento

@app.route('/')
def index():
    render_template('index.html')
