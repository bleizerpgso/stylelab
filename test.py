import pymysql

conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="6177", db="app"
)
print("conexión establecida")

def buscador(tags):
    return f"select marca, modelo from ropa where tags like '%{tags}%' "

tags = input("")
cursor = conn.cursor()
cursor.execute(
    buscador(tags)
)
for nombre, modelo in cursor.fetchall():
    print("{0} {1}".format(nombre, modelo))

