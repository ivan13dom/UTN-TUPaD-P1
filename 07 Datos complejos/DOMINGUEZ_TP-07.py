# 1) Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear lista de frutas sin precios
solo_frutas = list(precios_frutas.keys())
print("Lista de frutas:", solo_frutas)

# 4) Agenda telefónica
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre de un contacto para consultar su número: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5) Palabras únicas y conteo
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo_palabras)

# 6) Promedio de notas
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

# 7) Sets de estudiantes
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Stock de productos
stock = {}

producto = input("Ingrese el nombre del producto a consultar: ")
if producto in stock:
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    stock[producto] += cantidad
else:
    nuevo = int(input("Producto no encontrado. Ingrese stock inicial: "))
    stock[producto] = nuevo

print("Stock actualizado:", stock)

# 9) Agenda con tuplas (día, hora) -> evento
agenda_eventos = {}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
clave = (dia, hora)

if clave in agenda_eventos:
    print(f"Evento programado: {agenda_eventos[clave]}")
else:
    evento = input("No hay evento. Ingrese uno nuevo: ")
    agenda_eventos[clave] = evento
    print("Evento agregado.")

# 10) Invertir diccionario país → capital
paises = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario invertido:", capitales)
