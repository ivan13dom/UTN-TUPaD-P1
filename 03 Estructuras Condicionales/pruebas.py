contraseña = input("Ingrese una contraseña: ")
largo = len(contraseña)
if largo >= 8 and largo <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")