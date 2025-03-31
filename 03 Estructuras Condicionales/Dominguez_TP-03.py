#Ejecicio 1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print ("Es mayor de edad")

#Ejercicio 2
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprovado")
else:
    print("Desaprobado")

#Ejercicio 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un numero: "))
if (numero % 2) == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolecente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto")

#Ejercicio 5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contraseña = input("Ingrese una contraseña: ")
largo = len(contraseña)
if largo >= 8 and largo <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
#escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print (numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
#cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
elif media < mediana and media < moda:
    print("Sesgo negativo o a la izquierda")
#cuando la media, la mediana y la moda son iguales.
elif media == mediana == moda:
    print("Sin sesgo")

#Ejercicio 7
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
texto = input("Ingrese una frase o palabra: ")
if texto[-1] in "aeiou" or texto[-1] in "AEIOU":
    print(f"{texto}!")
else:
    print(texto)

#Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
opcion = input("Segun las siguientes opciones: \n 1.Si quiere su nombre en mayúsculas. \n 2.Si quiere su nombre en minúsculas \n 3.Si quiere su nombre con la primera letra mayúsculas. \n Ingrese la opcion que desea: ")
if opcion == "1":
    print(nombre.lower())
elif opcion == "2":
    print(nombre.upper())
elif opcion == "3":
    print(nombre.title())

#Ejercicio 9
#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
terremoto = int(input("Ingrese la magnitud del terremoto (del 1 al 7): "))
if  terremoto < 3:
    print("El terremoto fue Muy leve (imperceptible)")
elif terremoto == 3:
    print("El terremoto fue Leve (ligeramente perceptible)")
elif terremoto == 4:
    print("El terremoto fue Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto == 5:
    print("El terremoto fue Fuerte (puede causar daños en estructuras débiles)")
elif terremoto == 6:
    print("El terremoto fue Muy Fuerte (puede causar daños significativos)")
elif terremoto >= 7:
    print("El terremoto Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año, escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
emisferio = input("Ingrese el emisferio en el que se encuentra: ").title()
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))
#Primer condicional en caso de que el emisferio sea Norte
if emisferio == "Norte":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        estacion = "Otoño"
if emisferio == "Sur":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        estacion = "Primavera"
if emisferio not in ["Norte","Sur"]:
    print("El emisferio ingresado no es valido")
else:
    print(f"Su estacion en este momento es {estacion}")
