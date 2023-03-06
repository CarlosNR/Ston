import psycopg2

host = "localhost"
dbname = "Ston"
user = "postgres"
password = "001100"
# sslmode = "require"

#inicia conexao
conn_string = "host={0} user={1} dbname={2} password={3}".format(host,user,dbname,password)

#CLIENTES
def insereCliente(nome, nascimento, credito):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("insert into clientes (nome, nascimento, credito) values (%s, %s, %s) returning id;",(nome, nascimento, credito))
        conn.commit()

        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def deletaCliente(id):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("delete from clientes where id=%s;",(id, ))
        conn.commit()
    
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def adicionaCredito(id, credito):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("update clientes set credito = (credito + %s) where id = %s returning credito;",(credito, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def achaClientes():
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("select * from clientes order by id;")
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def achaCliente(id):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from clientes where id=%s;",(id, ))
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def login(id, nascimento):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from clientes where (id=%s and nascimento=%s);",(id, nascimento))
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
            
def achaClienteCredito(id):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select credito from clientes where id=%s;",(id, ))    
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def atualizaClienteCredito(id, preco):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update clientes set credito = (credito-%s) where id = %s;",(preco, id))    
        conn.commit()
    
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
#JOGOS
def insereJogo(nome, publicadora, maior18, genero, preco):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("insert into jogos (nome, publicadora, maior18, genero, preco) values (%s, %s, %s, %s, %s);",(nome, publicadora, maior18, genero, preco))
        conn.commit()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def atualizaPrecoJogo(id, preco):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
    
        cursor.execute("update jogos set preco = %s where id = %s;",(preco, id))    
        conn.commit()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
          
def achaJogos():
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from jogos order by nome;")
        return cursor.fetchall()
        
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def achaJogoNome(nome):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
    
        cursor.execute("select * from jogos where nome=%s;",(nome, ))
        return cursor.fetchone()
    
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def achaJogoId(id):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
    
        cursor.execute("select * from jogos where id=%s;",(id, ))
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
def achaJogoNomeParecido(nome):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        #caso 2 jogos tenham mesmo nome, ie street fighter 2 e street fighter 2 turbo edition
        cursor.execute("select * from jogos where position(%s in nome)>0;",(nome, ))
        return cursor.fetchall()
        
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
    
def deletaJogo(id):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
    
        cursor.execute("delete from jogos where id=%s returning nome;",(id, ))
        conn.commit()
        return cursor.fetchone()
        
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close
        
#COMPRAS
def insereCompra(idCliente, idJogo, dataCompra):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        dadoCliente = achaCliente(idCliente)
        credito = dadoCliente[3]
        dadoJogo = achaJogoId(idJogo)
        preco = dadoJogo[5]

        if (preco > credito):
            return False
        else:
            atualizaClienteCredito(idCliente, preco)
            cursor.execute("insert into compras (idcliente, idjogo, datacompra) values (%s, %s, %s);",(idCliente, idJogo, dataCompra))
            conn.commit()
            credito = achaClienteCredito(idCliente)
            return credito
            
    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def achaCompras(idCliente):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from compras where idCliente=%s;",(idCliente,))
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

# def exemplo():
#     try:
#         conn = psycopg2.connect(conn_string)
#         cursor = conn.cursor()

#         cursor.execute("algum comando")
#         conn.commit()

#     except psycopg2.DatabaseError as error:
#         cursor.execute("ROLLBACK")
#         conn.commit()

#     finally:
#         cursor.close()
#         conn.close
        
