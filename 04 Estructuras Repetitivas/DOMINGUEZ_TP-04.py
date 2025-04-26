#1)Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
num = 0
for num in range (101):
    print(num)

#2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

#Pedimos el numero al usuario
numero_entero = int(input("Ingresa un entero: "))

#Pasamos el numero a positivo por si ingresa uno negativo
numero_entero = abs(numero_entero)

#Contamos los caracteres del numero como si fuese un texto
cant_digitos = len(str(numero_entero))

#Mostramos el resultado por pantalla
print("La cantidad de digitos que tiene el numero es", cant_digitos)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#pedimos al usuario los valores
num1 = int(input("Ingrese el primer numero: ")) 
num2= int(input("Ingrese el segundo numero: "))

#agregamos condicional para avisarle al usuario como deben ser los valores (primer numero menos al segundo)
if num1>num2:
    print("Los valores no son correctos, el primer numero debe ser menor al segundo")
else:
    suma = 0
    for i in range(num1,(num2+1)):
        suma = suma + i
    print(suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0
num=1
while num!=0:
    num = int(input("Ingrese un numero: "))
    suma = suma + num
print("La suma de sus nuemeros es",suma)