from flask import Flask, request, render_template, session, redirect, jsonify
from flask_session import Session
from flask_bootstrap import Bootstrap5
from src.db import *
from datetime import date

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
bootstrap = Bootstrap5(app)

# Acesso
@app.errorhandler(404) 
def not_found(e): 
  return e

@app.route('/')
def index():
    if("idLogado" in session):
      dadosLogado = []
      dadosLogado.append(session["idLogado"])
      dadosLogado.append(session["nomeLogado"])
      dadosLogado.append(session["creditoLogado"])
      return render_template('/public/index.html', dadosLogado=dadosLogado)
    else:
      return render_template('/public/index.html')

@app.route('/read/cliente/logout', methods=['POST', 'GET'])
def logout():

    if("idLogado" in session):
        del session["idLogado"]
        del session["nomeLogado"]
        del session["creditoLogado"]

    return redirect('/')

# Clientes
@app.route('/insert/cliente')
def cliente():
    return render_template('/public/clientes/cadastraCliente.html')

@app.route('/insert/cliente', methods=['POST', 'GET'])
def cadastraClientes():

    nome = request.form['nome']
    nascimento = request.form['nascimento']
    
    credito = request.form['credito']
    senha = request.form['senha']
    email = request.form['email']

    print()
    print(nascimento)
    print()

    dados = insereCliente(nome, nascimento, credito, senha, email)

    return render_template('/public/clientes/cadastraCliente.html', dados=dados)

@app.route('/read/cliente')
def readCliente1():
    return render_template('/public/clientes/listaCliente.html')

@app.route('/read/cliente', methods=['POST', 'GET'])
def readCliente2():

    id = request.form['id']
    dadosUsuario = achaCliente(id)
    nomeJogos = []
    if (dadosUsuario):
      compras = achaCompras(id)
      if(compras):
        for compra in compras:
          jogo = achaJogoId(compra[2])
          nomeJogos.append(jogo[1])
        return render_template('/public/clientes/listaCliente.html', dadosUsuario=dadosUsuario, nomeJogos=nomeJogos)
      else:
        return render_template('/public/clientes/listaCliente.html', dadosUsuario=dadosUsuario)
    else:
      nenhum = True
      return render_template('/public/clientes/listaCliente.html', nenhum=nenhum)

@app.route('/read/clientes')
def listaClientes():

    if("mensagemCreditar" in session):
      mensagemCredita = session["mensagemCreditar"]  
      del session["mensagemCreditar"]
      listaClientes = achaClientes()
      return render_template('/public/clientes/listaClientes.html', listaClientes=listaClientes, mensagemCredita=mensagemCredita)

    listaClientes = achaClientes()
    return render_template('/public/clientes/listaClientes.html', listaClientes=listaClientes)

@app.route('/read/cliente/login')
def login1():
    return render_template('/public/clientes/logaCliente.html')

@app.route('/read/cliente/login', methods=['POST', 'GET'])
def login2():

    email = request.form['email']
    senha = request.form['senha']
    dados = login(email, senha)
    if (dados):
      session["idLogado"] = dados[0]
      session["nomeLogado"] = dados[1]
      session["creditoLogado"] = dados[3]
      return redirect("/")
    else:
      return render_template('/public/clientes/logaCliente.html', nenhum=True)

@app.route('/update/cliente/credito/<int:id>/<float:saldoAntigo>', methods=['POST', 'GET'])
def creditar1(id, saldoAntigo):

     return render_template('/public/clientes/credita.html', id=id, saldoAntigo=saldoAntigo)

@app.route('/update/cliente/credito/<int:id>/valor', methods=['POST', 'GET'])
def creditar2(id):

    if request.method == "POST":
      
      creditoAdicional = request.form['creditoAdicional']
      #fetchone retorna vetor msm se tiver apenas 1 item
      saldo = adicionaCredito(id, creditoAdicional) 
      session["mensagemCreditar"] = "O cliente de id %s teve seus creditos adicionados em %.2f e está com %.2f de saldo" % (id, float(creditoAdicional), float(saldo[0]))

    return redirect('/read/clientes')

@app.route('/delete/cliente/<idApagado>', methods=['POST', 'GET'])
def excluiCliente(idApagado):
  deletaCliente(idApagado)
  listaClientes = achaClientes()
  return render_template('/public/clientes/listaClientes.html', idApagado=idApagado, listaClientes=listaClientes)

#Jogos
@app.route('/insert/jogo')
def jogo1():
    return render_template('public/jogos/cadastraJogo1.html')

@app.route('/insert/jogo', methods=['POST', 'GET'])
def insereJogo1():
 
  session["nomeJogo"] = request.form['nome']
  session["publicadora"] = request.form['publicadora']
  session["maior18"] = request.form['maior18']
  session["genero"] = request.form['genero']
  session["preco"] = request.form['preco']

  if (achaJogoNome(session["nomeJogo"])):
    mensagem = "Jogo com nome identico já incluso, cadastro falhou."
    return render_template('/public/jogos/cadastrajogo1.html', mensagem=mensagem)

  else:
    repetidos = achaJogoNomeParecido(session["nomeJogo"]) 
    
    if (repetidos):
      return render_template('/public/jogos/cadastrajogo2.html', repetidos=repetidos)
    else:
      mensagem = "Jogo cadastrado com sucesso."
      insereJogo(session["nomeJogo"], session["publicadora"], session["maior18"], session["genero"], session["preco"])  

      del session["nomeJogo"]
      del session["publicadora"]
      del session["maior18"]
      del session["genero"]
      del session["preco"]

      return render_template('/public/jogos/cadastrajogo1.html', mensagem=mensagem)

@app.route('/insert/jogo/pt2')
def jogo2():
    return render_template('/public/jogos/cadastrajogo2.html')

@app.route('/insert/jogo/pt2', methods=['POST', 'GET'])
def cadastraJogos():

  nomeJogo = session["nomeJogo"]
  publicadora = session["publicadora"]
  maior18 = session["maior18"]
  genero = session["genero"]
  preco = session["preco"]

  insereJogo(nomeJogo, publicadora, maior18, genero, preco)  
  mensagem = "Jogo cadastrado com sucesso."

  del session["nomeJogo"]
  del session["publicadora"]
  del session["maior18"]
  del session["genero"]
  del session["preco"]

  return render_template('/public/jogos/cadastrajogo1.html', mensagem=mensagem)

@app.route('/read/jogos')
def listaJogos():

    listaJogos = achaJogos()

    if("mensagemPrecificar" in session):
      mensagemPrecificar = session["mensagemPrecificar"]  
      del session["mensagemPrecificar"]
      return render_template('/public/jogos/listaJogos.html', listaJogos=listaJogos, mensagemPrecificar=mensagemPrecificar)
      
    if("mensagemErroDeleteJogo" in session):
      mensagemErroDeleteJogo = session["mensagemErroDeleteJogo"]
      del session["mensagemErroDeleteJogo"]
      return render_template('/public/jogos/listaJogos.html', listaJogos=listaJogos, mensagemErroDeleteJogo=mensagemErroDeleteJogo)
  
    return render_template('/public/jogos/listaJogos.html', listaJogos=listaJogos)

@app.route('/read/jogo')
def readJogo1():

    if("idLogado" in session):
      dadosLogado = []
      dadosLogado.append(session["idLogado"])
      dadosLogado.append(session["nomeLogado"])
      dadosLogado.append(session["creditoLogado"])
    else:
      dadosLogado = False

    listaTodosJogos = achaJogos()

    if(listaTodosJogos == ""):
        return render_template('/public/jogos/listaJogo.html', dadosLogado=dadosLogado, algum=True)
    else:
       return render_template('/public/jogos/listaJogo.html', dadosLogado=dadosLogado, algum=False)


@app.route('/read/jogo', methods=['POST', 'GET'])
def readJogo2():
    
    listaComprados = []
    if("idLogado" in session):
      dadosLogado = []
      dadosLogado.append(session["idLogado"])
      dadosLogado.append(session["nomeLogado"])
      dadosLogado.append(session["creditoLogado"])

      comprados = achaCompras(session["idLogado"])

      if(comprados):

        for comprado in comprados:
            listaComprados.append(comprado[2])

    else:
      dadosLogado = False

    nome = request.form['nome']
    jogos = achaJogoNomeParecido(nome)    
    if (jogos):
      return render_template('/public/jogos/listaJogo.html', jogos=jogos, dadosLogado=dadosLogado, listaComprados=listaComprados)
    else:
      jogoEspecifico=True
      return render_template('/public/jogos/listaJogo.html', jogoEspecifico=jogoEspecifico, dadosLogado=dadosLogado, listaComprados=listaComprados)
      
@app.route('/update/jogo/preco/<int:id>', methods=['POST', 'GET'])
def precificar1(id):
    jogo = achaJogoId(id)
    return render_template('/public/jogos/precifica.html', id=id, preco=jogo[5])

@app.route('/update/jogo/preco/<int:id>/<float:preco>', methods=['POST', 'GET'])
def precificar2(id,preco):

  novoPreco = request.form['novoPreco']
  atualizaPrecoJogo(id, novoPreco) 
  jogo = achaJogoId(id)
  session["mensagemPrecificar"] = "O jogo %s teve seu valor modificado de %.2f para %.2f" % (jogo[1], float(preco), float(novoPreco))
  return redirect('/read/jogos')

@app.route('/delete/jogo/<idApagado>', methods=['POST', 'GET'])
def excluiJogo(idApagado):

    existe = achaJogoId(idApagado)
    
    if existe:
        nome = deletaJogo(idApagado)
        listaJogos = achaJogos()

        if(nome != None):
          mensagemDeleteJogo = "O jogo "+nome[0]+" foi deletado com sucesso."
          return render_template('/public/jogos/listaJogos.html', idApagado=idApagado, mensagemDeleteJogo=mensagemDeleteJogo, listaJogos=listaJogos)

        if(nome == None):
          session["mensagemErroDeleteJogo"] = "Jogo não pode ser apagado pois alguem já comprou."  
          return redirect('/read/jogos')

    else:
        session["mensagemErroDeleteJogo"] = "Jogo não pode ser apagado pois não existe mais no sistema."
        return redirect('/read/jogos')

   

#Compras
@app.route('/insert/compra/<int:idJogo>/<string:nomeJogo>/<float:preco>', methods=['POST', 'GET'])
def cadastraCompra(idJogo,nomeJogo,preco):
    
    if request.method == "POST":

      if("idLogado" in session):
      
        dadosLogado = []
        dadosLogado.append(session["idLogado"])
        dadosLogado.append(session["nomeLogado"])
        dadosLogado.append(session["creditoLogado"])

        comprados = achaCompras(session["idLogado"])

        if(comprados):
          for comprado in comprados:
            if(idJogo == comprado[2]):
              mensagemCompraFalha = "Compra não realizada: cliente já passui o jogo em sua lista de compras."
              return render_template('/public/jogos/listaJogo.html', mensagemCompraFalha = mensagemCompraFalha, dadosLogado=dadosLogado)
        
        result = insereCompra(session["idLogado"], idJogo, date.today())

        if(result):
          session['creditoLogado'] = result[0]
          dadosLogado[2]=(session["creditoLogado"])

          mensagemCompraSucesso="%s foi inserido em tua lista de jogos!",(nomeJogo, )
          return render_template('/public/jogos/listaJogo.html', nomeJogo=nomeJogo,mensagemCompraSucesso=mensagemCompraSucesso, dadosLogado=dadosLogado)
        else:
          mensagemCompraFalha = "Compra não realizada: credito insuficiente."
          return render_template('/public/jogos/listaJogo.html', mensagemCompraFalha = mensagemCompraFalha, dadosLogado=dadosLogado)
 
    else:
        # Caso o espertinho entre pelo link mesmo sem ter botão disponivel
        return render_template('/public/jogos/listaJogo.html', dadosLogado=False)

#Validadores
@app.route('/insert/cliente/valida/email', methods=['GET', 'POST'])
def validaEmail():

  if request.method == "POST":
    email = request.get_json()['email'].strip()
    
    resp = achaClienteEmail(email)
    if (resp):
      return jsonify({"emailRepetido": "true"})
    else:
      return jsonify({"emailRepetido": "false"})