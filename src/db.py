import psycopg2

host = "localhost"
dbname = "Ston"
user = "postgres"
password = "001100"
# sslmode = "require"

#inicia conexao
conn_string = "host={0} user={1} dbname={2} password={3}".format(host,user,dbname,password)

conn = psycopg2.connect(conn_string)
print("conexão deu bom")

cursor = conn.cursor()

#clientes
def insereCliente(nome, nascimento, credito):

    cursor.execute("insert into clientes (nome, nascimento, credito) values (%s, %s, %s) returning id;",(nome, nascimento, credito))
    conn.commit()
    return cursor.fetchone()
def deletaCliente(id):
    cursor.execute("delete from clientes where id=%s;",(id, ))
    conn.commit()
def adicionaCredito(id, credito):
    cursor.execute("update clientes set credito = (credito + %s) where id = %s returning credito;",(credito, id))
    conn.commit()
    return cursor.fetchone()
def achaClientes():
    cursor.execute("select * from clientes;")
    return cursor.fetchall()
def achaCliente(id):
    cursor.execute("select * from clientes where id=%s;",(id, ))
    return cursor.fetchone()

#jogos
def insereJogo(nome, publicadora, maior18, genero, preco):

    cursor.execute("insert into jogos (nome, publicadora, maior18, genero, preco) values (%s, %s, %s, %s, %s);",(nome, publicadora, maior18, genero, preco))
    conn.commit()
def atualizaPrecoJogo(id, preco):
    cursor.execute("update jogos set preco = %s where id = %s;",(preco, id))    
    conn.commit()
    
def achaJogos():
    cursor.execute("select * from jogos;")
    return cursor.fetchall()

def achaJogoNome(nome):
    cursor.execute("select * from jogos where nome=%s;",(nome, ))
    return cursor.fetchone()

def achaJogoId(id):
    cursor.execute("select * from jogos where id=%s;",(id, ))
    return cursor.fetchone()

def achaJogoNomeParecido(nome):
    #caso 2 jogos tenham mesmo nome, ie street fighter 2 e street fighter 2 turbo edition
    cursor.execute("select * from jogos where position(%s in nome)>0;",(nome, ))
    return cursor.fetchall()
    
def deletaJogo(id):
    cursor.execute("delete from jogos where id=%s;",(id, ))
    conn.commit()

#compras
def insereCompra(idcliente, idjogo, datacompra):
    cursor.execute("insert into compra (idcliente, idjogo, datacompra) values (%s, %s, %s);",(idcliente, idjogo, datacompra))
    conn.commit()
def achaCompras(idCliente):
    cursor.execute("select * from compra where idCliente=%s;",(idCliente,))
    return cursor.fetchall()

#encerra conexao
# cursor.close()
# conn.close