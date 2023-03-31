import time
import pymysql
conn = pymysql.connect(
    host="localhost", port=3306, user="root",
    passwd="6177", db="app"
)
print("conexión establecida")

def buscador(tags):
    return f"select marca, modelo from ropa where tags like '%{tags}%' "




print("Elije entre estas 3 marcas de ropa:")
print("polo ralph lauren (1)")
print("Nike(2)")
print("Primark(3)")
seleccion_1= int(input("Marca a escoger: "))

print("Ahora te pondremos otras marcas de ropa relacionadas con tu selección:")
time.sleep(2)



if seleccion_1 == 1:
    seleccion_1 = "cayetano"
    print("Lacoste(1)")
    print("Calvin Klein(2)")
    print("Guess(3)")
    seleccion_cayetano = int(input("Marca a escoger: "))
elif seleccion_1 == 2:
    seleccion_1 = "deporte"
elif seleccion_1 == 3:
    print("H&M(1)")
    print("Levi's(2)")
    print("Desigual(3)")
    seleccion_perrofla = int(input("Marca a escoger: "))

cursor = conn.cursor()
cursor.execute(
    buscador(seleccion_1)
)
for nombre, modelo in cursor.fetchall():
    print("{0} {1}".format(nombre, modelo))
