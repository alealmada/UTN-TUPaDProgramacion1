# # 1) Crear una lista con las notas de 10 estudiantes.

# # • Mostrar la lista completa.

# lista_notas = [10,8,6,3,4,3,7,8,9,10]


# for i in range(len(lista_notas)):

#     print(lista_notas[i])


# # • Calcular y mostrar el promedio.


# suma=0 

# promedio=0

# for i in range(len(lista_notas)):

#     suma += lista_notas[i]

# promedio= suma / len(lista_notas)

# print("El promedio es: ", promedio)


# # • Indicar la nota más alta y la más baja.


# for indice_pasado in range(len(lista_notas)-1 ):

#     for indice_actual in range(len(lista_notas)-1 - indice_pasado):

#         if lista_notas[indice_actual] > lista_notas[indice_actual +1]:

#             lista_notas[indice_actual], lista_notas[indice_actual +1] = lista_notas[indice_actual +1], lista_notas[indice_actual]


# nota_mas_alta= lista_notas[9]

# nota_mas_baja = lista_notas[0]


# print(f"La nota mas alta es: {nota_mas_alta}")

# print(f"La nota mas baja es: {nota_mas_baja}")


# 2) Pedir al usuario que cargue 5 productos en una lista.

# lista_productos = []

# for i in range(5):

#      lista_productos.append(input("Ingrese un producto: "))
# print(lista_productos)

# # • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().

# print("Lista ordenada.")
# print(sorted(lista_productos))

# # • Preguntar al usuario qué producto desea eliminar y actualizar la lista.


# #Preguntanos que producto se desea eliminar

# eliminar_producto = input("¿Que producto desea eliminar?: ")

# lista_productos.remove(eliminar_producto)

# #Mostramos lista actualizada 


# print("lista actualizada.")
# print(lista_productos)


# #Preguntamos que producto se quiere actualizar


# actualizar_producto = int(input("¿Que posicion desea actualizar?: "))

# nuevo_producto = input("Ingrese el nuevo producto: ")

# lista_productos[actualizar_producto] = nuevo_producto

# #Mostramos lista actualizada 

# print("lista actualizada.")
# print(lista_productos)


# # 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# import random 

# lista_numeros = []



# #CREAMOS UN CICLO FOR PARA COMPLETAR LA LISTA CON NUMEROS ALEATORIOS

# for i in range(15):
   

#     lista_numeros.append(random.randint(0, 99))

# print(lista_numeros)



# # • Crear una lista con los pares y otra con los impares.

# #LISTAS NUEVAS DE PARES E IMPARES
# lista_impares = []
# lista_pares = []

# #CREAMOS UN CICLO FOR PARA RECORRER LA LISTA Y SEPARAR PARES E IMPARES

# for i in range(len(lista_numeros)):

#     if lista_numeros[i] % 2 == 0:
#         (lista_pares).append(lista_numeros[i])

#     else :

#         lista_impares.append(lista_numeros[i])

# print("Lista pares: ")
# print(lista_pares)

# print("Lista impares: ")
# print(lista_impares)



# # • Mostrar cuántos números tiene cada lista.

# cantidad_pares = len(lista_pares)
# cantidad_impares = len(lista_impares)

# print(f"La lista de pares tiene: {cantidad_pares} numeros")
# print(f"La lista de impares tiene: {cantidad_impares} numeros")

# # 4) Dada una lista con valores repetidos:
# datos = [1,3,5,3,7,1,9,5,3]
# # • Crear una nueva lista sin elementos repetidos.

# lista_nuevos_datos= []
# print(datos)
# for i in range(len(datos)):            
#     repetido = False                   
#     for j in range(i):                
#         if datos[i] == datos[j]:       
#             repetido = True
#             break
#     if not repetido:                  
#         lista_nuevos_datos.append(datos[i])


# # • Mostrar el resultado.
# print(lista_nuevos_datos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# lista_estudiantes = ["Camila", "Juan", "Sofia", "Martin", "Valentina", "Lucas", "Micaela", "Agustin"]

# accion = input("¿Quiere eliminar o agregar un nombre a la lista? Escriba agregar/borrar: ").lower()

# if accion == "agregar" :
#     nuevo_nombre = input("Ingrese el nuevo nombre: ") 
#     lista_estudiantes.append(nuevo_nombre)
# elif accion == "borrar":
#     eliminar_nombre = input("ingrese el nombre que quiere eliminar: ")
#     if eliminar_nombre in lista_estudiantes :
#         lista_estudiantes.remove(eliminar_nombre)
#     else:
#         print("El nombre no se encuentra en la lista")
# print("Lista actualizada")
# print(lista_estudiantes)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

# lista_numeros = [1, 2, 3, 4, 5, 6, 7]

# ultimo = lista_numeros[-1]     #GUARDAMOS EL ULTIMO ELEMENTO
# #CREAMOS UN FOR QUE RECORRE DESDE EL PRIMER AL ULTIMO        
# for i in range(len(lista_numeros)-1, 0, -1):  
#     lista_numeros[i] = lista_numeros[i-1]     #ITERAMOS Y MOVEMOS UNO A LA DERECHA
# lista_numeros[0] = ultimo             

# print(lista_numeros)

# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

# temperaturas_semanales =[
# [1,4],
# [6,8],
# [2,8],
# [6,7],
# [1,12],
# [1,10],
# [3,20],
#  ] 

# print(temperaturas_semanales)

# promedio_minimas = 0
# suma_minimas = 0

# promedio_maximas = 0
# suma_maximas = 0
# for i in range(7):
#     suma_minimas += temperaturas_semanales [i][0]
#     suma_maximas += temperaturas_semanales [i][1]
# promedio_minimas = suma_minimas / 7   
# promedio_maximas = suma_maximas / 7 
# print(f"El promedio de las temperaturas minimas es: {promedio_minimas}")
# print(f"El promedio de las temperaturas maxima es: {promedio_maximas}")


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.


