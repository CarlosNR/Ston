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

def insereCliente(nome, nascimento, credito):

    cursor.execute("insert into clientes (nome, nascimento, credito) values (%s, %s, %s);",(nome, nascimento, credito))
    conn.commit()

def deletaExemplo(campoId):
    cursor.execute("delete from nomeTabela where id=%s;",(campoId))
    conn.commit()

def atualizaCampoExemplo(campoId, campoAtualizado):
    cursor.execute("update nomeTabela set colunaAtualizada = %s where id = %s;",(campoAtualizado, campoId))

def findAllExemplo():
    cursor.execute("select * from nomeTabela;")
    conn.commit()
    return cursor.fetchall()

def findExemplo(campoId):
    cursor.execute("select * from nomeTabela where campoId=%s;",(campoId))
    conn.commit()
    return cursor.fetchall

#encerra conexao
# cursor.close()
# conn.close