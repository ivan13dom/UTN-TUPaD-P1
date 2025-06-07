#1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

#Funciones
def imprimir_hola_mundo(mensaje):
    return (print(mensaje))


#Programa principal
imprimir_hola_mundo("Hola mundo")

#2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#Funciones
def saludar_usuario(mensaje):
    return (print(f"Hola, {mensaje}!"))


#Programa principal
saludar_usuario("Marcos")


#3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados

#Funciones
def informacion_personal(nombre, apellido, edad, residencia):
     print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

#Programa principal
nombre = input("Ingrese un nombre: ")
apellido = input("Ingrese un apellido: ")   
edad= int(input("Ingrese una edad: "))
residencia = input("Ingrese una residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4)Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#Primero importamos la libreria math para obtener las constantes matematicas, en este caso utilizaremos Pi
import math

#Funciones
def calcular_area_circulo(radio):
    return math.pi *(radio**2)

def calcular_perimetro_circulo(radio):
    return (2* math.pi* radio)

#Programa principal
radio = float(input("Ingrese un radio: "))

print(f"El area es {calcular_area_circulo(radio)} y su perimetro es {calcular_perimetro_circulo(radio)}")


# 5)Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#Funciones
def segundos_a_horas(segundos):
    return (segundos/60)/60

def validar_segundos(segundos_a_validar):
    while segundos_a_validar < 1:
        segundos_a_validar = float(input("ERROR. Ingrese la cantidad de segundos que desea convertir en horas: "))
    return segundos_a_validar

#Programa principal
segundos = float(input("Ingrese segundos: "))
segundos = validar_segundos(segundos)

print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas")


# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero*i
        print(f"{numero} X {i} = {resultado}")

#Programa principal
numero = float(input("Ingrese un numero: "))

tabla_multiplicar(numero)


# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#Funciones
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return(suma, resta, multiplicacion,division)


#Programa principal
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
resultados = operaciones_basicas(num1, num2)

print(f"{num1} + {num2} = {resultados[0]}")
print(f"{num1} - {num2} = {resultados[1]}")
print(f"{num1} * {num2} = {resultados[2]}")
print(f"{num1} / {num2} = {resultados[3]}")


# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#Funciones
def calcular_imc(peso, altura):
    return peso /(altura**2)


#Programa principal
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (mts): "))

print(f"Su indice de masa corporal es {calcular_imc(peso, altura):.2f}")


# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.


#Funciones
def celsius_a_fahrenheit(celsius):
    return (((celsius * 9)/5)+32)

#Programa principal
grados_c = float(input("Ingrese la temperatura en °C (Celsius): "))

print(f"{grados_c}°C equivalen a {celsius_a_fahrenheit(grados_c):.2f}°F")


# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.


#Funciones
def calcular_promedio(a, b, c):
   return (a+b+c)/3

#Programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el ultimo numero: "))

print(f"El promedio de sus numeros es {calcular_promedio(num1,num2,num3):.2f}")