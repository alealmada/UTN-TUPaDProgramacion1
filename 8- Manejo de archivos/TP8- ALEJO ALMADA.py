print("1. Escribiendo archivo")
archivo_productos = open("productos.txt", "w")
archivo_productos.write("\nLapicera")
archivo_productos.write("\nPincel")
archivo_productos.close

print("2. Leyendo archivo")
archivo_productos = open("productos.txt", "r")
contenido = archivo_productos.read()
print(contenido)
archivo_productos.close

print("3. Agregando texto al final del archivo.")
archivo_productos = open("productos.txt", "a")
archivo_productos.write("Goma")
archivo_productos.close

print("4. Sobrescribiendo contenido")
archivo_productos = open("productos.txt", "w")
archivo_productos.write("Regla\n")
archivo_productos.close


print("2. Leyendo archivo")
archivo_productos = open("productos.txt", "r")
contenido = archivo_productos.read()
print(contenido)
archivo_productos.close

print("9. Leyendo archivo con with")
with  open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

print("10. Creando contenido con with")
with open("productos.txt", "a") as archivo:
    archivo.write("\nCartuchera")

print("11. Leyendo texto")
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)