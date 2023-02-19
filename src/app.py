from flask import Flask, request, render_template, redirect
from src.db import *
from datetime import date

app = Flask(__name__)

# caso pg n exista
@app.errorhandler(404) 
def not_found(e): 
  return f"Saia dessa página imediatamente {e}"

# home
@app.route('/')
def index():
    return render_template('/public/index.html')

@app.route('/cadastraCliente')
def cliente():
    return render_template('/public/clientes/cadastraCliente.html')

# pós inputs
@app.route('/cadastraCliente', methods=['POST', 'GET'])
def cadastraClientes():

  nome = request.form['nome']
  nascimento = request.form['nascimento']
  credito = request.form['credito']

  insereCliente(nome, nascimento, credito)

  return "Cliente cadastrado com sucesso."

@app.route('/cadastraJogo')
def jogo():
    return render_template('/public/jogos/cadastraJogo.html')

# pós inputs
@app.route('/cadastraJogo', methods=['POST', 'GET'])
def cadastraJogos():

  nome = request.form['nome']
  publicadora = request.form['publicadora']
  maior18 = request.form['maior18']
  genero = request.form['genero']
  preco = request.form['preco']

  insereJogo(nome, publicadora, maior18, genero, preco)

  return "Cliente cadastrado com sucesso."
date.today()