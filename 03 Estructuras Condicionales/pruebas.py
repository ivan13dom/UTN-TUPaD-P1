nombre = input("Ingrese su nombre: ")
opcion = input("Segun las siguientes opciones: \n 1.Si quiere su nombre en mayúsculas. \n 2.Si quiere su nombre en minúsculas \n 3.Si quiere su nombre con la primera letra mayúsculas. \n Ingrese la opcion que desea: ")
if opcion == "1":
    print(nombre.lower())
elif opcion == "2":
    print(nombre.upper())
elif opcion == "3":
    print(nombre.title())