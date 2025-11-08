# ACLARACION : SE REALIZARON ALGUNOS ELJERCICIOS PARA REFORZAR LA UNIDAD NO LA TOTALIDAD.

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios

lista_frutas = []
for i in precios_frutas:
    lista_frutas.append(i) 
    
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}
for i in range(5):
    nuevo_contacto = input("Ingrese un nuevo contacto: ")
    nuevo_numero = input("Ingrese el numero telefonico: ")
    contactos[nuevo_contacto] = nuevo_numero
    

while True:
    buscar_nombre = input("Ingrese el nombre del contacto que busca: ")
    if buscar_nombre in contactos.keys():
        print(f"El numero es {contactos[buscar_nombre]}")
    else:
        print("El contacto no existe. Intente nuevavente")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Ingrese una frase separada por espacios: ")

#Colocamos todas las palabras en minusculas para evitar errores
frase = frase.lower()

#Separamos la frase en plabras
palabras = frase.split()

#Guardamos las palabras unicas
palabras_unicas = set(palabras)

#Creamos el diccionario
cantidad_palabras = {}

#Con un ciclo for contamos la cantidad de veces que se repte cada palabra

for palabra in palabras:
    if palabra in cantidad_palabras:
        cantidad_palabras[palabra] += 1
    else:
        cantidad_palabras[palabra] = 1

#Mostramos por pantalla

print("Palabras unicas: ")
print(palabras_unicas)

print("Cantidad de veces qie aparece cada palabra: ")
print(cantidad_palabras)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_almacen = {"Leche" : 12, "Queso" : 1, "Pan" : 3, "Gaseosa" : 0}

opcion = int(input("Ingrese 1 para consultar el stock, 2 para agregar unidades o 3 agregar un nuevo producto si no existe: "))

match opcion: 
    case 1:
        producto = input("Sobre cual producto quiere consultar?: ")
        print(f"El stock es: {stock_almacen[producto]}")

    case 2:
        producto = input("Sobre cual producto quie modificar el stock?: ")
        cantidad_nueva = int(input("Cual es el nuevo valor?: "))
        if producto in stock_almacen:
            stock_almacen[producto] += cantidad_nueva
    case 3:
        nuevo_producto = input("Cual es el nuevo producto que desea agregar?: ")
        cantidad_nueva = int(input("Cual es su stock?: "))
        stock_almacen[nuevo_producto] = cantidad_nueva
    
print(stock_almacen)
