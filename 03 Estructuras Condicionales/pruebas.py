edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolecente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto")