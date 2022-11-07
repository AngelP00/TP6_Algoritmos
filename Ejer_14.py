from grafo import Grafo


'''
14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
tareas:
'''

print('''
a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
''')

g = Grafo(dirigido=False)


g.insertar_vertice('cocina', datos={})
g.insertar_vertice('comedor', datos={})
g.insertar_vertice('cochera', datos={})
g.insertar_vertice('quincho', datos={})

g.insertar_vertice('banio 1', datos={})
g.insertar_vertice('banio 2', datos={})
g.insertar_vertice('habitacion 1', datos={})
g.insertar_vertice('habitacion 2', datos={})

g.insertar_vertice('sala de estar', datos={})
g.insertar_vertice('terraza', datos={})
g.insertar_vertice('patio', datos={})

print('''
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
es la distancia entre los ambientes, se debe cargar en metros;
''')

g.insertar_arista('cocina', 'comedor', 6)
g.insertar_arista('cocina', 'cochera', 3)
g.insertar_arista('cocina', 'quincho', 2)

g.insertar_arista('comedor', 'cochera', 2)
g.insertar_arista('comedor', 'quincho', 3)

g.insertar_arista('cochera', 'quincho', 2)

g.insertar_arista('banio 1', 'banio 2', 6)
g.insertar_arista('banio 1', 'habitacion 1', 3)
g.insertar_arista('banio 1', 'habitacion 2', 2)

g.insertar_arista('banio 2', 'habitacion 1', 6)
g.insertar_arista('banio 2', 'habitacion 2', 3)

g.insertar_arista('habitacion 1', 'habitacion 2', 3)

g.insertar_arista('sala de estar', 'banio 2', 6)
g.insertar_arista('sala de estar', 'terraza', 3)
g.insertar_arista('sala de estar', 'patio', 2)
g.insertar_arista('sala de estar', 'cochera', 2)
g.insertar_arista('sala de estar', 'banio 1', 4)

g.insertar_arista('terraza', 'habitacion 1', 3)
g.insertar_arista('terraza', 'habitacion 2', 2)

g.insertar_arista('patio', 'habitacion 1', 3)
g.insertar_arista('patio', 'habitacion 2', 11)

print(
'''
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
''')
arbol_min = g.kruskal()
print('Arbol de expansion minima:')
print(arbol_min)

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    #print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print('')
print('Determine cuantos metros de cables se necesitan para conectar todos los ambientes.')
#print(f"El peso total es {peso_total}")
print(f"Se necesitan {peso_total} metros de cable para conectar todos los ambientes.")


print('''
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv.
''')
vertice_a = 'habitacion 1'
vertice_b = 'sala de estar'

if g.existe_paso(vertice_a, vertice_b):
    resultados1 = g.dijkstra(vertice_a)
    camino = g.camino(resultados1, vertice_a, vertice_b)
    #print(camino)
    print('el camino mas corto es:',camino['camino'])
    print('se necesitan',camino['costo'],'metros de cable.')
    pass
else:
    print('no se puede llega de', vertice_a,' a',vertice_b)