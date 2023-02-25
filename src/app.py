from flask import Flask, request, render_template, session, redirect
from flask_session import Session
from src.db import *
from datetime import date

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# caso pg n exista
@app.errorhandler(404) 
def not_found(e): 
  return e

# home
@app.route('/')
def index():
    return render_template('/public/index.html')

# Clientes
@app.route('/insert/cliente')
def cliente():
    return render_template('/public/clientes/cadastraCliente.html')

# 
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
    if("mensagemCreditar" in session):
      mensagem = session["mensagemCreditar"]  
      del session["mensagemCreditar"]
      listaClientes = achaClientes()
      return render_template('/public/clientes/listaClientes.html', listaClientes=listaClientes, mensagem=mensagem)

    listaClientes = achaClientes()
    return render_template('/public/clientes/listaClientes.html', listaClientes=listaClientes)

@app.route('/update/cliente/credito/<int:id>/<float:credito>', methods=['POST', 'GET'])
def creditar1(id, credito):
    
    return render_template('/public/clientes/credita.html', id=id, credito=credito)

@app.route('/update/cliente/credito/<int:id>', methods=['POST', 'GET'])
def creditar2(id):

  creditoAdicional = request.form['creditoAdicional']
  #fetchone retorna vetor msm se tiver apenas 1 item
  saldo = adicionaCredito(id, creditoAdicional) 
  print()
  print(saldo)
  print()
  session["mensagemCreditar"] = "O cliente de id %s teve seus creditos adicionados em %.2f e está com %.2f de saldo" % (id, float(creditoAdicional), float(saldo[0]))

  return redirect('/read/clientes')

@app.route('/delete/cliente/<idApagado>', methods=['POST', 'GET'])
def excluiCliente(idApagado):
  deletaCliente(idApagado)
  listaClientes = achaClientes()
  return render_template('/public/clientes/listaClientes.html', idApagado=idApagado, listaClientes=listaClientes)

#Jogos
@app.route('/insert/jogo/pt1')
def jogo1():
    return render_template('/public/jogos/cadastraJogo1.html')

@app.route('/insert/jogo/pt1', methods=['POST', 'GET'])
def insereJogo1():
 
  session["nome"] = request.form['nome']
  nome = session["nome"]
  session["publicadora"] = request.form['publicadora']
  session["maior18"] = request.form['maior18']
  session["genero"] = request.form['genero']
  session["preco"] = request.form['preco']

  if (achaJogo(nome)):
    mensagem = "Jogo com nome identico já incluso, cadastro falhou."
    return render_template('/public/jogos/cadastrajogo1.html', mensagem=mensagem)

  else:
    repetidos = achaJogoNomeParecido(nome) 
    
    if (repetidos):
      return render_template('/public/jogos/cadastrajogo2.html', repetidos=repetidos, )
    else:
      mensagem = "Jogo cadastrado com sucesso."
      return render_template('/public/jogos/cadastrajogo1.html', mensagem=mensagem)

@app.route('/insert/jogo/pt2')
def jogo2():
    return render_template('/public/jogos/cadastrajogo2.html')

@app.route('/insert/jogo/pt2', methods=['POST', 'GET'])
def cadastraJogos():

  nome = session["nome"]
  publicadora = session["publicadora"]
  maior18 = session["maior18"]
  genero = session["genero"]
  preco = session["preco"]

  insereJogo(nome, publicadora, maior18, genero, preco)  
  mensagem = "Jogo cadastrado com sucesso."

  del session["nome"]
  del session["publicadora"]
  del session["maior18"]
  del session["genero"]
  del session["preco"]

  return render_template('/public/jogos/cadastrajogo1.html', mensagem=mensagem)

@app.route('/read/jogos')
def listaJogos():
    if("mensagemPrecificar" in session):
      mensagem = session["mensagemPrecificar"]  
      del session["mensagemPrecificar"]
      listaJogos = achaJogos()
      return render_template('/public/jogos/listaJogos.html', listaJogos=listaJogos, mensagem=mensagem)
      
    listaJogos = achaJogos()
    return render_template('/public/jogos/listaJogos.html', listaJogos=listaJogos)

@app.route('/update/jogo/preco/<int:id>', methods=['POST', 'GET'])
def precificar1(id):
    jogo = achaJogoId(id)
    return render_template('/public/jogos/precifica.html', id=id, preco=jogo[5])

@app.route('/update/jogo/preco/<int:id>/<float:preco>', methods=['POST', 'GET'])
def precificar2(id,preco):

  novoPreco = request.form['novoPreco']
  atualizaPrecoJogo(id, novoPreco) 
  jogo = achaJogoId(id)
  session["mensagemPrecificar"] = "O jogo %s teve seu valor modificado de %.2f para %.2f" % (jogo[2], float(preco), float(novoPreco))
  return redirect('/read/jogos')

@app.route('/delete/jogo/<idApagado>', methods=['POST', 'GET'])
def excluiJogo(idApagado):
  deletaJogo(idApagado)
  listaJogos = achaJogos()
  return render_template('/public/jogos/listaJogos.html', idApagado=idApagado, listaJogos=listaJogos)