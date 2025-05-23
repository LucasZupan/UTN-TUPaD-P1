class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = {}

    def agregar_hijo(self, nodo):
        self.hijos[nodo.valor] = nodo


    def buscar_camino(self, destino, camino=None):
        if camino is None:
            camino = []

        camino.append(self.valor)

        if self.valor == destino:
            return camino

        for hijo in self.hijos.values():
            camino_encontrado = hijo.buscar_camino(destino, camino[:])
            if camino_encontrado:
                return camino_encontrado

        return None

# 1) Basándose en el método buscar_camino de la clase Nodo provista en el notebook, crear una nueva clase Nodo que contenga el método calcular_longitud_de_camino.
#  El mismo debe, a partir del camino encontrado, calcular la longitud de camino. Si es imposible encontrar un camino debe retornar None. 

    def calcular_longitud_de_camino(self, destino):
        
        camino = self.buscar_camino(destino)       
        if camino:
            return len(camino) - 1    
        return None


# 2) Partiendo de la clase Nodo creada en la actividad anterior, modificarla para incluir los siguientes métodos: 
#   ● obtener_hijos: debe imprimir por pantalla si el nodo tiene hijos y, en caso de tener, cuáles nodos son. 
#   ● obtener_padre: debe imprimir por pantalla si el nodo tiene padre y, en caso de tener, cuál nodo es. 
#   ● obtener_tipo: debe imprimir por pantalla si el nodo es raíz, rama u hoja. Puede usar los métodos anteriores.

    def obtener_hijos(self):
      if self.hijos:
        hijos = list(self.hijos.keys())
        return hijos
      return None

    def obtener_padre(self, raiz):
        camino_a_la_raiz = raiz.buscar_camino(self.valor)
        if len(camino_a_la_raiz) == 1:
          return None
        padre = camino_a_la_raiz[-2]
        return padre

    def obtener_tipo(self, raiz):
      hijos = self.obtener_hijos()
      padres = self.obtener_padre(raiz)
      if hijos:
        if padres:
          return "Nodo rama"
        else:
          return "Nodo raiz"
      return "Nodo hoja"
# 3) Basándose en la clase ArbolBusquedaBinario provista en el notebook, crear una nueva clase ArbolBusquedaBinario que contenga el método buscar_nodo, 
# el cual debe recibir el valor de un nodo y buscarlo en el árbol binario para ver si éste lo contiene o no. 

class ArbolBusquedaBinario:
    def __init__(self):
        self.raiz = None

    def imprimir_arbol(self):
        if self.raiz is None:
            print("El árbol está vacío.")
        else:
            self._imprimir_arbol(self.raiz, "", True)

    def _imprimir_arbol(self, nodo, espacio, es_izquierda):
        if nodo is None:
            return
        self._imprimir_arbol(nodo.derecha, espacio + "   ", False)
        print(espacio + ("└── " if es_izquierda else "├── ") + str(nodo.valor))
        self._imprimir_arbol(nodo.izquierda, espacio + "   ", True)


    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)

        else:
            self._insertar(self.raiz, valor)


    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)

        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)


    def buscar_nodo(self, valor):
        return self._buscar_nodo(self.raiz, valor)

    def _buscar_nodo(self, nodo, valor):
        if nodo is None:
            return False  # Valor no encontrado
        if valor == nodo.valor:
            return True  # Valor encontrado

        # Si el valor a buscar es menor, buscamos en el subárbol izquierdo
        if valor < nodo.valor:
            return self._buscar_nodo(nodo.izquierda, valor)

        # Si el valor a buscar es mayor, buscamos en el subárbol derecho
        return self._buscar_nodo(nodo.derecha, valor)
    
# 4) Crear dos funciones: 
#   ● crear_listas_adyacencia_dirigida: debe tomar como input los nodos y aristas de un grafo dirigido y retornar las listas de adyacencia de cada nodo. 
#   ● crear_matriz_adyacencia_dirigida: debe tomar como input los nodos y aristas de un grafo dirigido y retornar la matriz de adyacencia del grafo.
#  Nota: deberá utilizar una convención para nombrar las aristas. Por ejemplo, podría nombrarse primero el nodo de origen y el nodo de destino. 
# Si la arista se dirige de Y hacia Z (Y → Z) la arista sería (Y, Z).
 
def crear_listas_adyacencia_dirigida(nodos, aristas):
  
  listas_adyacencia = {}
  for nodo in nodos:
    listas_adyacencia[nodo] = []

  
  for u, v in aristas:
    listas_adyacencia[u].append(v)

  return listas_adyacencia


def crear_matriz_adyacencia_dirigida(nodos, aristas):
  # Inicializamos la matriz de adyacencia
  cantidad_nodos = len(nodos)
  matriz_adyacencia = [[0] * cantidad_nodos for _ in range(cantidad_nodos)]

  # Respetando la convención para nombrar aristas, debemos colocar 1 únicamente
  # cuando el nodo es el origen de la arista
  for u, v in aristas:
    u_index = nodos.index(u)
    v_index = nodos.index(v)

    matriz_adyacencia[u_index][v_index] = 1

  return matriz_adyacencia
 
#  5) Probar las funciones creadas en el punto anterior usando el siguiente grafo: B -> A -> C

nodos = ['A', 'B', 'C']
aristas = [('B', 'A'), ('A', 'C')]

print(crear_listas_adyacencia_dirigida(nodos, aristas))
print(crear_matriz_adyacencia_dirigida(nodos, aristas))

