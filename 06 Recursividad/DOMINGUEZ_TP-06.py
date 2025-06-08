# 1) Factorial recursivo e impresión de factoriales del 1 al n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular los factoriales del 1 al número ingresado: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Fibonacci recursivo y mostrar la serie hasta n
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

limite = int(input("Ingrese hasta qué posición desea ver la serie de Fibonacci: "))
for i in range(limite + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")

# 4) Conversión de decimal a binario (recursivo)
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es {binario if binario else '0'}")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra para verificar si es un palíndromo: ")
print(f"¿Es palíndromo? {es_palindromo(texto)}")

# 6) Suma de dígitos de un número (recursivo, sin convertir a string)
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

numero_suma = int(input("Ingrese un número para sumar sus dígitos: "))
print(f"La suma de los dígitos de {numero_suma} es {suma_digitos(numero_suma)}")

# 7) Contar bloques en una pirámide (recursivo)
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques del nivel inferior: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# 8) Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero_busqueda = int(input("Ingrese un número: "))
digito_busqueda = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito_busqueda} aparece {contar_digito(numero_busqueda, digito_busqueda)} veces en {numero_busqueda}")
