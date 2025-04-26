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

suma = 0 #definimos la variable que guardara el resultado de la suma
num=1 #definimos num como 1 para que el ciclo se ejecute desde el inicio
while num!=0:
    num = int(input("Ingrese un numero: "))
    suma = suma + num
print("La suma de sus nuemeros es",suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#definimos la variable que sera la respuesta correcta, en este caso 8
resp_correcta = 8

#Pedimo un numero al usuario
resp = int(input("Adivine el numero entre 0 y 9: "))
intentos = 1

#condicional para entrar a un buble o no
if resp == resp_correcta:
    print("Felicitaciones, acertaste en el primer intento, el numero era",resp)
else:
    while resp != resp_correcta:
        if resp < 0 or resp >9:
            print("Ese numero no es correcto. Recorda que tiene que estar entre 0 y 9")
        else:
            print ("Ese no es el numero correcto")
        resp = int(input("Intenta nuevamente: "))
        intentos+=1
    print("Felicitaciones, es el numero correcto, intentaste",intentos,"veces.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range (100, 0, -2):
    print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero_positivo = int(input("Ingrese un numero positivo: ")) #el usuario ingresa un numero
suma = 0 #iniciamos la suma en 0

#Entramos en un bucle si el numero es negativo hasta que el usuario de un nuemero positivo
while numero_positivo < 0:
    numero_positivo = int(input("El numero debe ser positivo: "))

#Una vez que es positivo se hace la suma
for i in range (numero_positivo+1):
    suma = suma +i
print("La suma es ", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)

#Inicializamos todos los contadores en 0
pares = 0
impares = 0
negativos= 0
positivos= 0

#Entramos en el bucle para que el usuario ingrese todos los numeros y se cuente cada categoria
for i in range (100):
    numero = int(input("Ingrese un numero "))
    if numero%2 == 0:
        pares= pares +1
    if numero%2 != 0:
        impares= impares +1
    if numero> 0:
        positivos= positivos +1
    if numero< 0:
        negativos= negativos +1
print("Los numero pares son ",pares)
print("Los numero impares son",impares)
print("Los numero negativos son",negativos)
print("Los numero positivos son",positivos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

suma = 0 #inicializamos la suma
limite=5
for i in range (limite):
    numero = int(input("Ingrese un numero: "))
    suma+=numero

print("La media es", (suma/limite))


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Pedimos al usuario que ingrese un número
numero = input("Ingrese un número: ")

# Invertimos el número usando
numero_invertido = numero[::-1]

# Mostramos el resultado
print("El número invertido es:", numero_invertido)
