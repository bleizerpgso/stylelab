import mysql.connector

mysql = mysql.connector.connect(
    host="localhost", user="root",
    passwd="6177", db="app"
)



print("conexión establecida")
def buscador(id, marca, modelo, precio, tags):
    return f"insert into ropa values ('{id}','{marca}','{modelo}', '{precio}' ,'{tags}');"

id = (input("Introduce el id: "))
marca = (input("Introduce la marca: "))
modelo = (input("Introduce el modelo: "))
precio = (input("Introduce el precio: "))
tags = (input ("Tag de la prenda: "))

cursor = mysql.cursor()
cursor.execute(
    buscador(id, marca, modelo, precio, tags)
)

mysql.commit()
