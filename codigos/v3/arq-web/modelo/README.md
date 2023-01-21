
# Aplicação Flask + arquitetura modelo 

## Passos para inicializar a aplicação

Acesse o diretório _**`modelo`**_ e execute os seguintes comandos no terminal:
```
$ python3 -m venv .venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ flask create-db
$ flask populate-db
$ flask add-user -u <digite um usuário> -p <digite uma senha>
```

## Executando a aplicação
```
$ flask run
```

Agora basta acessar a aplicação através do navegador pelo endereço http://127.0.0.1:5000
