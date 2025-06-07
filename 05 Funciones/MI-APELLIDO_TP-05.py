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