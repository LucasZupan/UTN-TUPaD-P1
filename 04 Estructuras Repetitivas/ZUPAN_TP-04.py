# Práctico 4: Estructuras Repetitivas

# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un numero entero "))
digitos = 1
while num > 9:
    digitos += 1
    num = num // 10
print(f"La cantidad de digitos es: {digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

min = int(input("Introduce el limite inferior: "))
max = int(input("Introduce el limite superior: "))
if min > max:
    min, max = max, min
suma = sum(range(min + 1, max))
print("La suma de los números enteros entre", min, "y", max, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total 
# acumulado cuando el usuario ingrese un 0.

num = int(input("Ingrese un numero entero: "))
suma = 0
while num != 0:
    suma = suma + num
    num = int(input("Ingrese otro numero entero o 0 para ver el acumulado: "))
print(f"El acumulado ingresado es: {suma}")    

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)
intentos = 0
while True:    
    intento_usuario = int(input("Adivina el número entre 0 y 9: "))    
    intentos += 1  
    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intenta de nuevo.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Introduce un número entero positivo: "))
suma = sum(range(num + 1))  
print(f"La suma de todos los números entre 0 y {num} es: {suma}")

# 8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos 
# números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa 
# puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(100):
    numero = int(input(f"Introduce el número {i + 1}: ")) 
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
 
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números positivos: {positivos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

suma = 0
for i in range(100):
    num = int(input(f"Introduce el número {i + 1}: ")) 
    suma += num   
print(f"La media es: {suma / 100}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Introduce un número: ")
num_invertido = num[::-1]
print(f"El número invertido es: {num_invertido}")