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
