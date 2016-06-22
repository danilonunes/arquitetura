from flask import Flask, url_for

app = Flask('myapporm')

n_version = 0
n_release = 0
n_build = 1

txt_versao = '{0}.{1}.{2}'.format(n_version, n_release, n_build)

base_html = """
    <html>
        <link rel=stylesheet type=text/css href="{css_file}">
        <head>
            <title>{title}</title>
        </head>
        <div class=main>
            <body>
                <div class=header>
                    <a href="/"> <img src="{logo_url}" /> </a>
                    <h1>CEapp</h1>
                    <hr />
                </div>
                {body}
                <hr />
                <em>Versão {versao}</em>
            </body>
        </div>
    </html>
"""

login_html = '''
  <h2>Controle de Acesso</h2>
  <form action="{action_login}" method=post>
    <dl>
      <dt>Usuário:
      <dd><input type=text name=username>
      <dt>Senha:
      <dd><input type=password name=password>
      <dd><input type=submit value=Login>
    </dl>
  </form>
'''

@app.route('/')
def index():
    return base_html.format(
        title = 'Controle de Estoque Python 3 + Flask',
        css_file = 'static/style.css',
        logo_url = 'static/img/76671427304708.jpeg',
        body = '<h2>Exemplo de webapp em Flask</h2><form action="login"><input type=submit value=Login>',
        versao = txt_versao)
    
@app.route('/login')
def login():
    return base_html.format(
        title = 'Controle de Estoque Python 3 + Flask',
        css_file = 'static/style.css',
        logo_url = 'static/img/76671427304708.jpeg',
        body = login_html,
        versao = txt_versao)

if __name__ == '__main__':
    import os
    app.run(host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)