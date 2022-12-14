import os
from collections import deque
cola = deque()
print(cola)
deque([])
visitados = []

grafo = {'a': [('d',1),('f',2),('g',3)],
         'd': [('a',1),('h',4),('c',5)],
         'f': [('a',2),('b',6),('i',7)],
         'g': [('a',3)],
         'h': [('d',4),('k',8)],
         'c': [('d',5),('j',9)],
         'b': [('f',6),('l',8)],
         'i': [('f',7),('m',7),('n',6)],
         'k': [('h',8)],
         'j': [('c',9),('x',10)],
         'l': [('b',8),('z',11)],
         'm': [('i',7)],
         'n': [('i',6)],
         'x': [('j',10)],
         'z': [('l',11)],
}

print("Muestra el grafo a evaluar: \n")
for key, lista in grafo.items():
    print(key)
    print(lista)

origen = input("Ingresa un el nodo que sera el origen: ")
print("\nLista de recorrido en lo ancho del arbol\n")

cola.append(origen)

while cola:

    actual = cola.popleft()
    
    if actual not in visitados:
        print("Vertice actual ->", actual)
        visitados.append(actual)
    for key, lista in grafo[actual]:
             if key not in visitados:
                    cola.append(key)
