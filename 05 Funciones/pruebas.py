# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.


#Funciones
def calcular_promedio(a, b, c):
   return (a+b+c)/3

#Programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el ultimo numero: "))

print(f"El promedio de sus numeros es {calcular_promedio(num1,num2,num3)}")