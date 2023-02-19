from flask import Flask, request, render_template, redirect
from src.db import *
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
