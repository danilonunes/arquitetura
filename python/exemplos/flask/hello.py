from flask import Flask # importando do módulo Flask a classe Flask

#app = Flask(__name__) # maneira pouco elegante

app = Flask("hello_world") # maneira elegante

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/br/")
def hello_br():
    return "Olá mundo!"

if __name__ == "__main__":
    app.run()
