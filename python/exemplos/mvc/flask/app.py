from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    mensagem = 'Esse é um outro teste!'
    return render_template('index.html', msg=mensagem)
