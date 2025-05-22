# 1) Escribe una función busqueda_lineal(lista, objetivo) que recorra la lista y devuelva el índice del elemento si se encuentra, o -1 si no está. 
# Luego, prueba la función con la lista [10, 20, 30, 40, 50] y busca el número 30.

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# 2) Modifica la función de búsqueda lineal para contar cuántas comparaciones realiza antes de encontrar el número 50 en [10, 20, 30, 40, 50].

def busqueda_lineal_contando(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            print("Comparaciones realizadas:", comparaciones)
            return i
    print("Comparaciones realizadas:", comparaciones)
    return -1

# 3) Implementa la función busqueda_binaria(lista, objetivo), que tome una lista ordenada y devuelva el índice del elemento encontrado o -1 si no está.
#  Luego, pruébala con la lista [1, 3, 5, 7, 9, 11, 13, 15] para buscar el número 7.

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# 4) Modifica la búsqueda binaria para contar cuántos pasos se necesitan para encontrar el número 11 en [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21].

def busqueda_binaria_contando(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    pasos = 0

    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            print("Pasos realizados:", pasos)
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    print("Pasos realizados:", pasos)
    return -1

# 5) Genera una lista de 20 números aleatorios entre 1 y 100. Luego, implementa una búsqueda lineal que intente encontrar el número 50 en la lista generada.
import random

lista_aleatoria = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista_aleatoria)

resultado = busqueda_lineal(lista_aleatoria, 50)
if resultado != -1:
    print(f"Número 50 encontrado en índice: {resultado}")
else:
    print("Número 50 no encontrado en la lista.")

# 6) Usa sorted() para ordenar la lista generada en el ejercicio anterior y luego busca el número 50 usando búsqueda binaria. 
# lista_ordenada = sorted(lista) print(lista_ordenada)

lista_ordenada = sorted(lista_aleatoria)
print("Lista ordenada:", lista_ordenada)
busqueda_binaria(lista_aleatoria, 50)

# 7) Escribe una función que cuente cuántas veces aparece el número 5 en la lista [1, 5, 2, 5, 3, 5, 4, 5]. 

def contar_ocurrencias(lista, numero):
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    return contador

# 8)Genera una lista ordenada de 10,000 números y mide el tiempo que tarda la búsqueda lineal y la búsqueda binaria en encontrar un número. 
# Usa time.time() para medir el tiempo.

import time

lista_grande = list(range(10000))
objetivo = 9999  # Puedes cambiar este valor para probar otros casos

inicio_lineal = time.time()
indice_lineal = busqueda_lineal(lista_grande, objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal


inicio_binaria = time.time()
indice_binaria = busqueda_binaria(lista_grande, objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria


print(f"Búsqueda lineal encontró el número en el índice {indice_lineal} en {tiempo_lineal:.8f} segundos.")
print(f"Búsqueda binaria encontró el número en el índice {indice_binaria} en {tiempo_binaria:.8f} segundos.")

# 9) Los diccionarios en Python permiten búsquedas eficientes. Crea un diccionario con nombres como claves y edades como valores. 
# Luego, escribe una función que busque una edad dada y devuelva el nombre asociado.

personas = {"Alice": 25, "Bob": 30, "Charlie": 22}
def buscar_por_edad(diccionario, edad):
    for nombre, valor in diccionario.items():
        if valor == edad:
            return nombre
    return None  # Si no se encuentra la edad




