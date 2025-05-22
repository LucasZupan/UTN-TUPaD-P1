# Trabajo Práctico: Análisis de Algoritmos

# Objetivo: Determinar la complejidad temporal de diferentes algoritmos utilizando la notación Big-O. Comparar distintas soluciones para un mismo problema y analizar cuál es más eficiente.

# Instrucciones:
# 1. Analiza cada algoritmo y determina su orden de complejidad T(n) y O(n).
# 2. Justifica tu respuesta indicando los pasos relevantes en el análisis.
# 3. En los ejercicios 1 y 2, compara ambas soluciones y argumenta cuál es más eficiente.

# Ejercicio 1: Suma de los primeros n números
def suma_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

#Pregunta: ¿Cuál es el orden de complejidad de esta función? Explica tu respuesta.
# El orden de complejidad de este algoritmo es:
#       T(n) = c x n 
#       O(n)
# Es un bucle que itera desde 1 hasta n realizando una suma en cada iteracion, por lo que la cantidad de operaciones depende de n.

# Ejercicio 2: Suma de los primeros n números
def suma_numeros_formula(n):
    return (n * (n + 1)) // 2

# Pregunta: ¿Cuál es el orden de complejidad de esta función? ¿Cuál de las dos soluciones (Ejercicio 1 o 2) es más eficiente? Explica por qué.
#La complejidad de este algoritmo es:
#       T(n): c
#       O(1)
# El tiempo no depende de variables, es constante. Por lo tanto esta solucion es mas eficiente que la del ejercicio 1. Se puede apreciar la diferencia en velocidad para valores grandes de n.

#Ejercicio 3: Búsqueda de un elemento en una lista desordenada
def buscar_elemento(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False
#Pregunta: Determina el peor caso y la complejidad temporal de este algoritmo.

#El peor caso es si el elemento no esta en la lista, por lo que la complejidad de este algoritmo es:
#       T(n): c x n
#       O(n) 


#Ejercicio 4: Encontrar el número máximo en una lista
def encontrar_maximo(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo
#Pregunta: ¿Cuál es el orden de complejidad de este algoritmo?
#La complejidad de este algoritmo es:
#       T(n) = c x n 
#       O(n)
# Siempre hay que recorrer todos los elementos de la lista por lo que la complejidad es proporcional a n.

#Ejercicio 5: Ordenamiento por selección
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
#Pregunta: Determina la complejidad temporal de este algoritmo y explica su comportamiento en el peor caso.
#La complejidad de este algoritmo es:
#       T(n) = n x (n-1) / 2 
#       O(n) = n^2
# El algoritmo consta de 2 ciclo for anidados por lo que su complejidad es cuadratica.