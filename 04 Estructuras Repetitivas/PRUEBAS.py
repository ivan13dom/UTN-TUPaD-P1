#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

suma = 0 #inicializamos la suma
limite=5
for i in range (limite):
    numero = int(input("Ingrese un numero: "))
    suma+=numero

print("La media es", (suma/limite))
