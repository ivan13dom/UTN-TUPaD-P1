# Trabajo Integrador - Árboles con listas (versión con números)

# Esta función crea un nodo del árbol. Cada nodo es una lista:
# [valor, subárbol izquierdo, subárbol derecho]
def crear_nodo(valor):
    return [valor, None, None]

# Inserta un valor en el árbol comparando con el nodo actual.
# Si es menor, va a la izquierda; si no, a la derecha.
def insertar_nodo(arbol, valor):
    if arbol is None:
        return crear_nodo(valor)
    if valor < arbol[0]:
        arbol[1] = insertar_nodo(arbol[1], valor)  # izquierda
    else:
        arbol[2] = insertar_nodo(arbol[2], valor)  # derecha
    return arbol

# Recorre el árbol en orden: izquierda → valor → derecha
def inorden(arbol):
    if arbol is not None:
        inorden(arbol[1])
        print(arbol[0])
        inorden(arbol[2])

# Recorre el árbol en preorden: valor → izquierda → derecha
def preorden(arbol):
    if arbol is not None:
        print(arbol[0])
        preorden(arbol[1])
        preorden(arbol[2])

# Recorre el árbol en postorden: izquierda → derecha → valor
def postorden(arbol):
    if arbol is not None:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0])

# Programa principal

# Lista de números a insertar en el árbol
numeros = [50, 30, 70, 20, 40, 60, 80]

# Árbol vacío al comienzo
arbol = None

# Insertamos los números uno por uno
for numero in numeros:
    arbol = insertar_nodo(arbol, numero)

# Mostramos los recorridos
print("Recorrido Inorden:")
inorden(arbol)

print("\nRecorrido Preorden:")
preorden(arbol)

print("\nRecorrido Postorden:")
postorden(arbol)
