#Imports
import time
import pymysql

#Conexión con el mysql
conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="6177", db="app"
)
print("conexión establecida")

#funcion para filtrar la ropa en mysql
def buscador(tags):
    return f"select id, marca, modelo from ropa where tags like '%{tags}%' "

# Selección de las 3 primeras marcas de ropa
print("Elije entre estas 3 marcas de ropa:")
print("H&M (1)")
print("Nike(2)")
print("Polo Ralph Lauren(3)")
primario= int(input("Marca a escoger: "))
primera_seleccion = {1: "casual", 2:"deporte", 3:"pijo"}

print("Ahora te pondremos otras marcas de ropa relacionadas con tu selección:")
time.sleep(2)


if primario == 1:
    print("Zara(1)")
    print("Primark(2)")
    print("Pull and Bear(3)")
    secundario = int(input("Ahora de estas 3 marcas selecciona la que mas te guste: "))
    segunda_seleccion = {1: "elegante", 2:"señora", 3:"joven"}
elif primario == 2:
    print("Adidas(1)")
    print("The North Face(2)")
    print("Jordan(3)")
    secundario = int(input("Ahora de estas 3 marcas selecciona la que mas te guste: "))
    segunda_seleccion = {1: "futbol", 2:"montaña", 3:"basquet"}
elif primario == 3:
    print("Stone Island(1)")
    print("Loius Vuitton(2)")
    print("Lacoste(3)")
    secundario = int(input("Ahora de estas 3 marcas selecciona la que mas te guste: "))
    segunda_seleccion = {1: "cayetano", 2:"exclusivo", 3:"comun"}




print (segunda_seleccion[secundario])
print (primera_seleccion[primario])

#Hace la consulta mysql a la funcion
cursor = conn.cursor()
cursor.execute(
    buscador("calle")
)
for id, nombre, modelo in cursor.fetchall():
    print("{0} {1}".format(nombre, modelo))
    id_ropa = id