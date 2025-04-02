# Práctico 3: Estructuras condicionales

# Actividades
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Ingrese su nota: "))
print("Aprobado") if nota >= 6 else print("Desaprobado") 

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número: "))
print("Ha ingresado un número par") if num % 2 == 0 else print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
#  en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular 
# la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] mean(mi_lista) 
# 
# En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. 
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de 
# una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, 
# su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
# Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma: 
# import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

import random
from statistics import mode, median, mean

# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

# Imprimir resultados
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Resultado: {sesgo}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#   pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Este programa realiza operaciones sobre dos numeros enteros ingresados distintos de 0")
num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 - num2}")

# 8) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
#  añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, 
#  dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase o palabra: ")
# Verificar si la última letra es una vocal (mayúscula o minúscula)
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

# Clasificar según la magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprimir el resultado
print(f"Clasificación: {categoria}")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año. 
# |           Periodo del año                                      | Estación en el hemisferio norte | Estación en el hemisferio sur |
# | Desde el 21 de diciembre hasta el 20 de marzo (incluidos)      |       Invierno                  |         Verano                |
# | Desde el 21 de marzo hasta el 20 de junio (incluidos)          |       Primavera                 |         Otoño                 |
# | Desde el 21 de junio hasta el 20 de septiembre (incluidos)     |       Verano                    |         Invierno              |
# | Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) |       Otoño                     |         Primavera             |
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Pedir datos al usuario
hemisferio = input("Ingrese el hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

# Validar el mes y el día
if mes < 1 or mes > 12:
    print("Mes no válido. Debe estar entre 1 y 12.")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dia = 31
    elif mes in [4, 6, 9, 11]:
        max_dia = 30
    else:  # Febrero (sin considerar año bisiesto)
        max_dia = 28

    if dia < 1 or dia > max_dia:
        print(f"Día no válido para el mes {mes}. Debe estar entre 1 y {max_dia}.")
    else:
        # Determinar estación según hemisferio y fecha
        if hemisferio == "N":
            if (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
                estacion = "Primavera"
            elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 23):
                estacion = "Verano"
            elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
                estacion = "Otoño"
            else:
                estacion = "Invierno"
        elif hemisferio == "S":
            if (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
                estacion = "Otoño"
            elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 23):
                estacion = "Invierno"
            elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
                estacion = "Primavera"
            else:
                estacion = "Verano"
        else:
            estacion = "Hemisferio no válido"

        # Imprimir resultado si la fecha y el hemisferio son válidos
        if hemisferio in ["N", "S"]:
            print(f"Estación del año: {estacion}")
        else:
            print("Hemisferio no válido. Debe ser 'N' o 'S'.")
