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
def buscador(tags, tags2):
    return f"select id, marca, modelo from ropa where tags like '%{tags}%' or tags like '%{tags2}%'"


# Selección de las 3 primeras marcas de ropa


print("""
SELECIONA ENTRE ESTAS 3 MARCAS ⤵

    +===============================+
    ||           H&M (1)           ||
    +===============================+
    ||           NIKE (2)          ||
    +===============================+
    ||           POLO (3)          ||
    +===============================+
""")
primario= int(input("Marca a escoger: "))
if primario == 1 or primario == 2 or primario == 3:
    primera_seleccion = {1: "casual", 2:"deporte", 3:"pijo"}
else:
    print("No es un numeor valido.")

print("Ahora te pondremos otras marcas de ropa relacionadas con tu selección:")
time.sleep(2)


if primario == 1:
    print("""
    +===============================+
    ||           ZARA (1)          ||
    +===============================+
    ||          PRIMARK (2)        ||
    +===============================+
    ||       PULL AND BEAR (3)     ||
    +===============================+
    """)
    secundario = int(input("Ahora de estas 3 marcas selecciona la que mas te guste: "))
    segunda_seleccion = {1: "elegante", 2:"señora", 3:"joven"}
elif primario == 2:
    print("""

    +===============================+
    ||          ADIDAS (1)         ||
    +===============================+
    ||      THE NORTH FACE (2)     ||
    +===============================+
    ||          JORDAN (3)         ||
    +===============================+

    """)
    secundario = int(input("Ahora de estas 3 marcas selecciona la que mas te guste: "))
    segunda_seleccion = {1: "futbol", 2:"montaña", 3:"basquet"}
elif primario == 3:
    print ("""
    +===============================+
    ||        STONE ISLAND (1)     ||
    +===============================+
    ||        LOUIS VUITTON (2)    ||
    +===============================+
    ||          LACOSTE (3)        ||
    +===============================+
    """)
    secundario = int(input("Ahora de estas 3 marcas selecciona la que mas te guste: "))
    segunda_seleccion = {1: "cayetano", 2:"exclusivo", 3:"comun"}

#Hace la consulta mysql a la funcion
cursor = conn.cursor()
cursor.execute(
    buscador("calle", "test")
)
for id, nombre, modelo in cursor.fetchall():
    print("{0} {1}".format(nombre, modelo))
    id_ropa = id