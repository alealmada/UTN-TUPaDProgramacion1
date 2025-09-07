# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

digitos = 0
numero_usuario= int(input("Ingrese un numero entero: "))
while numero_usuario > 0:
   numero_usuario = numero_usuario // 10
   digitos += 1
print(f"La cantidad de digitos es: {digitos}")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

suma = 0
valor_1= int(input("Ingrese el primer valor: "))
valor_2= int(input("Ingrese el siguiente valor: "))
 
for i in range(valor_1+1, valor_2):
    suma += i
print(f"La suma de los valores es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num_usuario = int(input("Ingresa un numero entero: "))
suma= num_usuario
while num_usuario != 0:
    num_usuario = int(input("Ingresa otro numero entero: "))
    suma += num_usuario
print(f"La suma de los numeros ingresados es: {suma}") 

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 
cant_intentos= 1
numero_aleatorio= random.randint(0, 9)
intento_usuario= int(input("Ingresa un numero del 0 al 9: "))
while intento_usuario != numero_aleatorio:
    cant_intentos += 1
    intento_usuario= int(input("Intentalo de nuevo: "))
print(f"Adivinaste! Necesitaste {cant_intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range (100, 0, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

suma= 0
num_usuario= int(input("Ingrese un numero: "))
for i in range(0, num_usuario+1):
    suma+=i
print(f"La suma de los numero es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_pares=0
cant_impares=0
cant_negativos=0
cant_positivos=0


for i in range(100):
    num_usuario= int(input("Ingrese un numero: "))
    # ACUMULACION DE PARES E IMPARES
    if num_usuario % 2 == 0:
        cant_pares+=1
    else:
        cant_impares+=1
    # ACUMULACION DE POSITIVOS Y NEGATIVOS
    if num_usuario > 0:
        cant_positivos+=1
    else:
        cant_negativos+=1
    
   
print("\nResumen de números ingresados:")
print(f"Pares: {cant_pares}")
print(f"Impares: {cant_impares}")
print(f"Positivos: {cant_positivos}")
print(f"Negativos: {cant_negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

CANTIDAD = 100  # SE PUEDE MODIFICAR CAMBIANDO UN SOLO VALOR
suma = 0

for i in range(CANTIDAD):
    num_usuario = int(input("Ingrese un número: "))
    suma += num_usuario

media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} números es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_usuario = int(input("Ingrese un número: "))
invertido = 0

while num_usuario > 0:
    digito = num_usuario % 10
    invertido = invertido * 10 + digito
    num_usuario = num_usuario // 10

print(f"El número invertido es: {invertido}")