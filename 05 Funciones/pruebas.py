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