from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'
    
@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    import os
    app.run(host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)