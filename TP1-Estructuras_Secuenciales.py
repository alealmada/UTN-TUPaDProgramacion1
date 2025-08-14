# TRABAJO PRACTICO 1 - TUPdD
# ALEJO ALMADA
#Se subira a GitHub

#Ejercicio 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#Ejercicio 2
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = str(input("Ingresa tu nombre: "))
print(f"¡Hola {nombre}!")

#Ejercicio 3
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = str(input("Ingresa tu nombre: "))
apellido = str(input("Ingresa tu apellido: "))
edad = int(input("¿Cual es tu edad?: "))
lugarResidencia = str(input("¿Donde vives?: "))
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}.")

#Ejercicio 4
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
pi = 3.14
radio = float(input("Ingrese el radio: "))
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"El area del ciculo es: {area} y su perimetro es: {perimetro}.")

# Ejercicio 5
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 60
print(f"La cantidad de segundos equivale a: {horas} hora/as.")


# Ejercicio 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

num = int(input("Ingrese un numero y se le devolvera su tabla de multiplicar: "))
print(num, "x 1= ",(num * 1))
print(num, "x 2= ",(num * 2))
print(num, "x 3= ",(num * 3))
print(num, "x 4= ",(num * 4))
print(num, "x 5= ",(num * 5))
print(num, "x 6= ",(num * 6))
print(num, "x 7= ",(num * 7))
print(num, "x 8= ",(num * 8))
print(num, "x 9= ",(num * 9))
print(num, "x 10= ",(num * 10))

# Ejercicio 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un numero, debe ser distinto de cero: "))
num2 = int(input("Ingrese otro numero, distinto de cero: "))
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1//num2
print(f"El resultado de sumar {num1} con {num2} es: {suma}.")
print(f"El resultado de restar {num1} con {num2} es: {resta}.")
print(f"El resultado de multiplicar {num1} con {num2} es: {mult}.")
print(f"El resultado de dividir {num1} con {num2} es: {div}.")

# Ejercicio 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

altura = float(input("Ingrese su altura en metros (Ej: 1.70): "))
peso = float(input("Ingrese su peso en kilogramos (Ej: 60): "))
imc = peso / (altura ** 2)
print(f"Tu IMC es de: {imc}.")

# Ejercicio 9
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. 

celsius =  float(input("Ingrese la tempreatura actual en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en fahrenheit es: {fahrenheit}.")

# Ejercicio 10
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los numeros ingresados es: {promedio}.")
