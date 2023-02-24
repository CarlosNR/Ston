from flask import Flask, request, render_template
from src.db import *
from datetime import date

app = Flask(__name__)

# caso pg n exista
@app.errorhandler(404) 
def not_found(e): 
  return e

# home
@app.route('/')
def index():
    return render_template('/public/index.html')

@app.route('/insert/cliente')
def cliente():
    return render_template('/public/clientes/cadastraCliente.html')

# pós inputs
@app.route('/insert/cliente', methods=['POST', 'GET'])
def cadastraClientes():

    nome = request.form['nome']
    nascimento = request.form['nascimento']
    credito = request.form['credito']

    dados = insereCliente(nome, nascimento, credito)

    return render_template('/public/clientes/cadastraCliente.html', dados=dados)

@app.route('/read/cliente')
def readCliente1():
    return render_template('/public/clientes/listaCliente.html')

# pós inputs
@app.route('/read/cliente', methods=['POST', 'GET'])
def readCliente2():

    id = request.form['id']
    dados = achaCliente(id)
    if (dados != None):
      compras = achaCompras(id)
      return render_template('/public/clientes/listaCliente.html', dados=dados, compras=compras)
    else:
      nenhum = True
      print()
      print(nenhum)
      print()
      return render_template('/public/clientes/listaCliente.html', nenhum=nenhum)
      
@app.route('/read/clientes')
def listaClientes():
    listaClientes = achaClientes()
    return render_template('/public/clientes/listaClientes.html', listaClientes=listaClientes)

@app.route('/update/cliente/credito/<int:id>/<float:credito>', methods=['POST', 'GET'])
def creditaUm(id, credito):
    
    return render_template('/public/clientes/credita.html', id=id, credito=credito)

@app.route('/update/cliente/credito/<int:id>', methods=['POST', 'GET'])
def creditaDois(id):

  creditoAdicional = request.form['creditoAdicional']
  adicionaCredito(id, creditoAdicional)  
  print(creditoAdicional)
  return "Creditado com sucesso."

@app.route('/delete/cliente/<idApagado>', methods=['POST', 'GET'])
def excluiCliente(idApagado):
  deletaCliente(idApagado)
  listaClientes = achaClientes()
  return render_template('/public/clientes/listaClientes.html', idApagado=idApagado, listaClientes=listaClientes)

@app.route('/insert/jogo')
def jogo():
    return render_template('/public/jogos/cadastraJogo.html')

# pós inputs
@app.route('/insert/jogo', methods=['POST', 'GET'])
def cadastraJogos():

  nome = request.form['nome']
  publicadora = request.form['publicadora']
  maior18 = request.form['maior18']
  genero = request.form['genero']
  preco = request.form['preco']

  insereJogo(nome, publicadora, maior18, genero, preco)

  return "Cliente cadastrado com sucesso."
date.today()