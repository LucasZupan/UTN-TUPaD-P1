# Práctico 1: Estructuras secuenciales

# Actividades
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#   el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#   por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#   realizar la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#   imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#   “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#   años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#   la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
lugar = input("Por favor ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

print("Este programa calcula el area de un circulo")
radio = int(input("Por favor ingrese el radio del circulo: "))
print(f"El radio es : {3.14*radio*radio}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

print("Este programa calcula a cuantas horas equivalen los segundos ingresados")
sec = int(input("Por favor ingrese una cantidad de segundos: "))
print(f"Los segundos ingresados equivalen a : {sec/3600} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

print("Este programa imprime la tabla de multiplicar del numero elegido")
num = int(input("Por favor ingrese un numero: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}") 

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#   pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Este programa realiza operaciones sobre dos numeros enteros ingresados distintos de 0")
num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 - num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#   de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#   𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2

print("Este programa calcula el Indice de Masa Corporal de una persona")
peso = float(input("Por favor ingrese el peso en kg: "))
altura = float(input("Por favor ingrese la altura en m: "))
print(f"El IMC = {peso/altura**2}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#   pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#   𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print("Este programa transforma una temperatura en grados Celsius a grados Fahrenheit")
temp = float(input("Por favor ingrese la temperatura en Celsius: "))
print(f"La temperatura en grados Farenheit es: {temp * 9 / 5 + 32}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

print("Este programa calcula el promedio de 3 numeros")
num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
num3 = int(input("Por favor ingrese el tercer numero: "))
print(f"El promedio de los 3 numeros es: {(num1 + num2 + num3)/3}")
