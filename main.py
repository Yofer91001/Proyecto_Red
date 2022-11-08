import clases
import funciones
import algoritmos


nodos = list()
aristas = list()
subredes = list()

for i in range(5):
  for j in range(4):
    nuevo_nodo = Node()
    nodos.append(nuevo_nodo)
    for k in range (j - 1):
      nueva_arista =  Edge()
      nuevo_nodo.aristas.append()
      
      if(nodos[i*4 + k + 1] != nuevo_nodo.ip):
        aristas.append(nueva_arista)
