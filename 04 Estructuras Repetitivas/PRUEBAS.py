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