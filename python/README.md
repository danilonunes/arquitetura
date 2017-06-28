# Como fazer um ambiente virtual - VirtualEnv

## Instalando o VirtualEnv no Debian e derivados

```
sudo apt update
sudo apt install virtualenv
sudo apt install python3-virtualenv
```

## Criando um ambiente virtual
```
virtualenv -p python3.5 [diretório]/meu_ambiente
```
O parâmetro ```-p``` informa para o VirtualEnv qual será o interpretador Python
usado pelo ambiente em questão (no exemplo é o Python 3.5). Caso não seja
informado esse parâmetro, o VirtualEnv definirá como interpretador o usado como
padrão pelo sistema operacional.


## Instalando o PIP - Python package manager - no Debian e derivados

```
sudo apt install pip
```

## Ativando o meu ambiente virtual
```
source [diretório]/meu_ambiente/bin/activate
```

Em caso de sucesso, o ambiente ativo será apresentado entre parêntese no início
da linha de comando.

Ex.:

```
   |
   V
(xmlrpc) danilonunes@server:~/Documentos/disciplinas/arquitetura/python$
```

## Desativando o meu ambiente virtual
```
deactivate
```

## Instalando pacotes através do pip
```
pip install nomeDoPacote
```

Ex.:
```
(xmlrpc) danilonunes@server:~$ pip install twisted
```

Caso você tenha um arquivo '''requirements.txt''' do software, pode realizar a
instalação de todas as bibliotecas necessárias (dependências) com um único
comando:

```
pip install -r requirements.txt
```

## Verificando os pacotes instalados no ambiente virtual

```
pip freeze
```

## Gerando o arquivo requirements.txt do meu projeto

```
pip freeze > requirements.txt
```
