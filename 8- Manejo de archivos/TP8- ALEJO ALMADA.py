# print("1. Escribiendo archivo")
# archivo_productos = open("productos.txt", "w")
# archivo_productos.write("\nLapicera")
# archivo_productos.write("\nPincel")
# archivo_productos.close

# print("2. Leyendo archivo")
# archivo_productos = open("productos.txt", "r")
# contenido = archivo_productos.read()
# print(contenido)
# archivo_productos.close

# print("3. Agregando texto al final del archivo.")
# archivo_productos = open("productos.txt", "a")
# archivo_productos.write("Goma")
# archivo_productos.close

# print("4. Sobrescribiendo contenido")
# archivo_productos = open("productos.txt", "w")
# archivo_productos.write("Regla\n")
# archivo_productos.close


# print("2. Leyendo archivo")
# archivo_productos = open("productos.txt", "r")
# contenido = archivo_productos.read()
# print(contenido)
# archivo_productos.close

# print("9. Leyendo archivo con with")
# with  open("productos.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)

# print("10. Creando contenido con with")
# with open("productos.txt", "a") as archivo:
#     archivo.write("\nCartuchera")

# print("11. Leyendo texto")
# with open("productos.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

archivo_inicial = open("productos.txt", "w")
archivo_inicial.write("nombre\n")
archivo_inicial.write("precio\n")
archivo_inicial.write("cantidad\n")
archivo_inicial.close

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,300.0,15\n")
    archivo.write("Goma,80.0,50\n")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        nombre, precio, cantidad = partes
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

nuevo_producto = input("Ingrese el nuevo producto con el siguiente formato: 'producto, precio, cantidad': ")

with open("productos.txt", "a") as archivo:
    archivo.write(nuevo_producto)

# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         linea = linea.strip()
#         partes = linea.split(",")
#         nombre, precio, cantidad = partes
#         print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")