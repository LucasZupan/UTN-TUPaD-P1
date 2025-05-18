# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en 
# pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número entero positivo: "))
if num < 1:
    print("Por favor, ingrese un número mayor o igual a 1.")
else:
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1   
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

limite = int(input("Ingrese la posición hasta la cual mostrar la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(limite + 1):
    print(f"F({i}) = {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑚(𝑚−1). 
# Prueba esta función en un algoritmo general.

def potencia(n, m):    
    if m == 0:
        return 1    
    else:
        return n * potencia(n, m - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calcular y mostrar el resultado
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):   
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True
#  si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):    
    if len(palabra) <= 1:
        return True
   
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):    
    if n < 10:
        return n

    return n % 10 + suma_digitos(n // 10)

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita 
# para construir toda la pirámide.

def contar_bloques(n):    
    if n == 1:
        return n

    return n + contar_bloques(n - 1)

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):    
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0

    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return 0 + contar_digito(numero // 10, digito)