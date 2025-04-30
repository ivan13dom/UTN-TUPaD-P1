#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

#Creamos la lista
lista_1_al_100 = list(range(4,101,4))
#Imprimimos la lista
print(lista_1_al_100)


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

#Creamos la lista
lista_5_elementos = ["Sillon","Heladera","TV",690,True]
#Slicing positivo
print(lista_5_elementos[4])
#Indexing negativo
print(lista_5_elementos[-1])


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

#Creamos la lista vacia
lista_vacia = []
#Añadimos los tres elementos
lista_vacia.append("unos")
lista_vacia.append("dos")
lista_vacia.append("tres")
#Cambiamos el nombre para ser mas claros
lista_3_elementos = lista_vacia
#Imprimimos
print(lista_3_elementos)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

#Creamos la lista
animales = ["perro", "gato", "conejo", "pez"]
#Reemplazamos los valores
animales [2] = "loro"
animales[-1] = "oso"
#Imprimimos el resultado
print(animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8,15,3,22,7]         #En primer lugar se crea la lista con los elementos 8, 15, 3, 22 y 7
numeros.remove(max(numeros))    #En esta linea se borra el valor maximo de la lista. En este caso 22
print(numeros)                  #Se imprime la lista como quedo despues de la modificacion


##6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

#Creamos la lista
lista_10_a_30 = list(range(10,31,5))
#Vemos como quedo la lista
print(lista_10_a_30)
#Imprimimos la consigna
print(lista_10_a_30[0:2])


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

#Creamos las lista
autos = ["sedan", "polo", "suran", "gol"]

#Reemplazamos los valores centrales
autos[1] = "kwid"
autos[2] = "ka"
#Imprimimos
print(autos)


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

#Creamos la lista vacia
dobles = []
#Agregamos los valores
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
#Imprimimos
print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

#Creamos la lista
compras = [["pan", "leche"], ["arros", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove ("pan")
#d) Imprimir la lista resultante por pantalla
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = []
#● Posición lista_anidada[0]: 15
lista_anidada.append(15)
#● Posición lista_anidada[1]: True
lista_anidada.append(True)
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
lista_anidada.append([25.5,57.9,30.6])
#● Posición lista_anidada[3]: False
lista_anidada.append(False)
#Imprimir la lista resultante por pantalla.
print(lista_anidada)