import pymysql

conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="6177", db="app"
)
print("conexión establecida")

def buscador(tags, tags2):
    return f"select id, marca, modelo from ropa where tags like '%{tags}%' or tags like '%{tags2}%'"

tags = "deporte"
tags2 = "calle"
cursor = conn.cursor()
cursor.execute(
    buscador(tags, tags2)
)

for id, nombre, modelo in cursor.fetchall():
    print("{0} {1}".format(nombre, modelo))
    id_ropa = id



