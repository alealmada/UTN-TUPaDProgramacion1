# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("¿Como es tu nombre?: ")
apellido = input("¿Como es tu apellido?: ")
edad = input("¿Cual es tu edad?: ")
residencia = input("¿Donde vives?: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como
# parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
# funciones para mostrar los resultados.

import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    if segundos < 3600: 
        print(f"{segundos} segundos corresponde a menos de una hora.")
    elif segundos >= 3600:
       horas =  segundos // 3600
       print(f"{segundos} segundos corresponden a {horas} horas")
        

segundos_usuario = int(input("Ingrese la cantidad de segundos: "))

segundos_a_horas(segundos_usuario)


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
   for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}x{i}= {resultado}")

num_usuario = int(input("Ingrese un numero: "))
tabla_multiplicar(num_usuario)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
#  Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a//b
    print(f"El resultado de sumar {a} con {b} es: {suma}.")
    print(f"El resultado de restar {a} con {b} es: {resta}.")
    print(f"El resultado de multiplicar {a} con {b} es: {mult}.")
    print(f"El resultado de dividir {a} con {b} es: {div}.")

num1 = int(input("Ingrese un numero, debe ser distinto de cero: "))
num2 = int(input("Ingrese otro numero, distinto de cero: "))

operaciones_basicas(num1, num2)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es de: {imc:.1f}") 

altura = float(input("Ingrese su altura en metros (Ej: 1.70): "))
peso = float(input("Ingrese su peso en kilogramos (Ej: 60): "))

calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en fahrenheit es: {fahrenheit}.")

celsius =  float(input("Ingrese la tempreatura actual en Celsius: "))
celsius_a_fahrenheit(celsius)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los numeros ingresados es: {promedio:.2f}")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el otro numero: "))
c = int(input("Ingrese el otro numero: "))

calcular_promedio(a, b, c)