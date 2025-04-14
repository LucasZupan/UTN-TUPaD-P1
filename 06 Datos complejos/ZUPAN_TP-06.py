#1) Dado el diccionario precios_frutas: 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#  Añadir las siguientes frutas con sus respectivos precios: 
#   ● Naranja = 1200 
#   ● Manzana = 1500 
#   ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas: 
#   ● Banana = 1330 
#   ● Manzana = 1700 
#   ● Melón = 2800 

precios_frutas["Banana"] = 13300
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios. 

frutas = list(precios_frutas.keys()) 
print(frutas)

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. 
# El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años." 

class Persona:  
  
  def __init__(self, nombre, pais, edad):
    self.nombre = nombre
    self.pais = pais
    self.edad = edad
  
  def saludar(self):
    print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")


# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. 
# Dichos métodos deben calcular el parámetro correspondiente.


from math import pi

class Circulo:
  
  def __init__(self, radio):
    self.radio = radio
 
  def calcular_area(self):
    area_circulo = pi * self.radio * self.radio
    return area_circulo

  def calcular_perimetro(self):
    perimetro_circulo = 2 * pi * self.radio
    return perimetro_circulo


#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.

def balanceado(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in expresion:
        if caracter in "({[":
            pila.append(caracter)
        elif caracter in ")}]":
            if not pila or pila.pop() != pares[caracter]:
                return False

    return len(pila) == 0


#7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: 
#   ● Agregar clientes (encolar). 
#   ● Atender clientes (desencolar). 
#   ● Mostrar el siguiente cliente en la fila. 

from collections import deque

class ColaBanco:
    def __init__(self):
        self.cola = deque()

    def encolar(self, cliente):
        self.cola.append(cliente)

    def desencolar(self):
        return self.cola.popleft() if self.cola else "No hay clientes"

    def siguiente_cliente(self):
        return self.cola[0] if self.cola else "No hay clientes"

# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados. 

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")



# 9) Dada una lista enlazada, implementa una función para invertirla. Ejemplo de entrada y salida:

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        prev = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = prev
            prev = actual
            actual = siguiente
        self.cabeza = prev