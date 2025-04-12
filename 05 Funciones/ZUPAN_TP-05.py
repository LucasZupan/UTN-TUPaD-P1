# Funciones de los ejercicios
#Ej 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Ej 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Ej 3
def informacion_personal(nombre, apellido, edad, lugar):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

#Ej 4
def calcular_area_circulo(radio):
    area = 3.14*radio*radio
    print(f"El area del circulo de radio {radio} es: {area}")

def calcular_perimetro_circulo(radio):
    perim = 3.14*radio*2
    print(f"El perimetro del circulo de radio {radio} es: {perim}")

#Ej 5
def segundos_a_horas(segundos):
    print(f"Los segundos ingresados equivalen a : {segundos/3600} horas.")

#Ej 6
def tabla_multiplicar(numero):    
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}") 

#Ej 7
def operaciones_basicas(a, b):
    print(f"{a} + {num2} = {a + b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} - {b} = {a - b}")

#Ej 8
def calcular_imc(peso, altura):
    print(f"El IMC = {peso/altura**2}")

#Ej 9
def celsius_a_fahrenheit(celsius):
    print(f"La temperatura en grados Farenheit es: {celsius * 9 / 5 + 32}")

#Ej 10
def calcular_promedio(a, b, c):
    print(f"El promedio de los 3 numeros es: {(a + b + c)/3}")




#Ejercicios
#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa 
# principal solicitando el nombre al usuario.

nombre = input("Como te llamas? :")
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy 
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = input("Por favor ingrese su edad: ")
lugar = input("Por favor ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, lugar)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

radio = float(input("Ingrese el radio del circulo a calcular: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad 
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

print("Este programa calcula a cuantas horas equivalen los segundos ingresados")
sec = int(input("Por favor ingrese una cantidad de segundos: "))
segundos_a_horas(sec)

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese 
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

num = int(input("Por favor ingrese un numero: "))
tabla_multiplicar(num)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
operaciones_basicas(num1, num2)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de 
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

peso = float(input("Por favor ingrese el peso en kg: "))
altura = float(input("Por favor ingrese la altura en m: "))
calcular_imc(peso, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en 
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

temp = float(input("Por favor ingrese la temperatura en Celsius: "))
celsius_a_fahrenheit(temp)

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.

num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
num3 = int(input("Por favor ingrese el tercer numero: "))
calcular_promedio(num1, num2, num3)
