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
    cursor.execute("update clientes set credito = (credito + %s) where id = %s;",(credito, id))
    conn.commit()
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

def atualizaNomeJogo(id, nome):
    cursor.execute("update jogos set nome = %s where id = %s;",(nome, id))
    conn.commit()
def atualizaPublicadoraJogo(id, publicadora):
    cursor.execute("update jogos set publicadora = %s where id = %s;",(publicadora, id))
    conn.commit()
def atualizaMaior18(id, maior18):
    cursor.execute("update jogos set maior18 = %s where id = %s;",(maior18, id))
    conn.commit()
def atualizaGeneroJogo(id, genero):
    cursor.execute("update jogos set genero = %s where id = %s;",(genero, id))    
    conn.commit()
def atualizaPrecoJogo(id, preco):
    cursor.execute("update jogos set preco = %s where id = %s;",(preco, id))    
    conn.commit()
def achaJogos():
    cursor.execute("select * from jogos;")
    return cursor.fetchall()
def achaJogo(nome):
    #caso 2 jogos tenham mesmo nome, ie street fighter 2 e street fighter 2 turbo edition
    cursor.execute("select *, position(('%s') in nome) from jogos where position('%s' in nome)>0;",(nome, nome))
    return cursor.fetchall

#compra
def insereCompra(idcliente, idjogo, datacompra):
    cursor.execute("insert into compra (idcliente, idjogo, datacompra) values (%s, %s, %s);",(idcliente, idjogo, datacompra))
    conn.commit()
def achaCompras(idCliente):
    cursor.execute("select * from compra where idCliente=%s;",(idCliente,))
    return cursor.fetchall()

#encerra conexao
# cursor.close()
# conn.close