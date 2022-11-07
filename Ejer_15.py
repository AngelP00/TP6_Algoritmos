from grafo import Grafo



'''
15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
'''
print('''
a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
uno en las naturales) y tipo (natural o arquitectónica);
''')
g = Grafo(dirigido=False)

# vertices
# ! maravillasnaturales
g.insertar_vertice('Cataratas del Iguazú', datos={'tipo': 'natural', 'pais': 'Argentina,Brasil'})
g.insertar_vertice('Amazonia', datos={'tipo': 'natural', 'pais': 'Bolivia,Brasil,Colombia,Ecuador,Guayana Francesa,Guyana,Perú,Surinam,Venezuela'})
g.insertar_vertice('Isla Jeju', datos={'tipo': 'natural', 'pais': 'Corea del Sur'})
g.insertar_vertice('Parque Nacional de Komodo', datos={'tipo': 'natural', 'pais': 'Indonesia'})
g.insertar_vertice('Río subterráneo de Puerto Princesa', datos={'tipo': 'natural', 'pais': 'Filipinas'})
g.insertar_vertice('Bahía de Ha Long', datos={'tipo': 'natural', 'pais': 'Vietnam'})
g.insertar_vertice('Montaña de la Mesa', datos={'tipo': 'natural', 'pais': 'Sudáfrica'})

#! maravillas arquitectonicas
g.insertar_vertice('Museo Guggenheim', datos={'tipo': 'arquitectonica_moderna', 'pais': 'España'})
g.insertar_vertice('Tokyo SkyTree', datos={'tipo': 'arquitectonica_moderna', 'pais': 'Japón'})
g.insertar_vertice('Centro Nacional de Artes Escénicas', datos={'tipo': 'arquitectonica_moderna', 'pais': 'China'})
g.insertar_vertice('Burj al Arab', datos={'tipo': 'arquitectonica_moderna', 'pais': 'Emiratos Arabes Unidos'})
g.insertar_vertice('Museo de Ciencias y Planetario de Nagoya', datos={'tipo': 'arquitectonica_moderna', 'pais': 'Japón'})
g.insertar_vertice('Edificio Cumulus', datos={'tipo': 'arquitectonica_moderna', 'pais': 'Dinamarca'})
g.insertar_vertice('El hotel Marina Bay Sands', datos={'tipo': 'arquitectonica_moderna', 'pais': 'Singapur'})



print('''
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
la distancia que las separa;
''')

# aristas
# ! maravillasnaturales
g.insertar_arista('Cataratas del Iguazú', 'Amazonia', 42341)
g.insertar_arista('Cataratas del Iguazú', 'Isla Jeju', 242343)
g.insertar_arista('Cataratas del Iguazú', 'Parque Nacional de Komodo', 232321)
g.insertar_arista('Cataratas del Iguazú', 'Río subterráneo de Puerto Princesa', 63422)
g.insertar_arista('Cataratas del Iguazú', 'Bahía de Ha Long', 63421)
g.insertar_arista('Cataratas del Iguazú', 'Montaña de la Mesa', 634212)

g.insertar_arista('Amazonia', 'Isla Jeju', 1521)
g.insertar_arista('Amazonia', 'Parque Nacional de Komodo', 12521)
g.insertar_arista('Amazonia', 'Río subterráneo de Puerto Princesa', 23453)
g.insertar_arista('Amazonia', 'Bahía de Ha Long', 25235)
g.insertar_arista('Amazonia', 'Montaña de la Mesa', 2523)

g.insertar_arista('Isla Jeju', 'Parque Nacional de Komodo', 3522)
g.insertar_arista('Isla Jeju', 'Río subterráneo de Puerto Princesa', 23532)
g.insertar_arista('Isla Jeju', 'Bahía de Ha Long', 2352)
g.insertar_arista('Isla Jeju', 'Montaña de la Mesa', 23523)

g.insertar_arista('Parque Nacional de Komodo', 'Río subterráneo de Puerto Princesa', 2352)
g.insertar_arista('Parque Nacional de Komodo', 'Bahía de Ha Long', 35432)
g.insertar_arista('Parque Nacional de Komodo', 'Montaña de la Mesa', 2352)

g.insertar_arista('Río subterráneo de Puerto Princesa', 'Bahía de Ha Long', 2352)
g.insertar_arista('Río subterráneo de Puerto Princesa', 'Montaña de la Mesa', 2352)

g.insertar_arista('Bahía de Ha Long', 'Montaña de la Mesa', 25232)

#! maravillas arquitectonicas
g.insertar_arista('Museo Guggenheim', 'Tokyo SkyTree', 2141)
g.insertar_arista('Museo Guggenheim', 'Centro Nacional de Artes Escénicas', 1241)
g.insertar_arista('Museo Guggenheim', 'Burj al Arab', 124)
g.insertar_arista('Museo Guggenheim', 'Museo de Ciencias y Planetario de Nagoya', 1241)
g.insertar_arista('Museo Guggenheim', 'Edificio Cumulus', 1421)
g.insertar_arista('Museo Guggenheim', 'El hotel Marina Bay Sands', 1421)

g.insertar_arista('Tokyo SkyTree', 'Centro Nacional de Artes Escénicas', 3242)
g.insertar_arista('Tokyo SkyTree', 'Burj al Arab', 3252)
g.insertar_arista('Tokyo SkyTree', 'Museo de Ciencias y Planetario de Nagoya', 432)
g.insertar_arista('Tokyo SkyTree', 'Edificio Cumulus', 4234)
g.insertar_arista('Tokyo SkyTree', 'El hotel Marina Bay Sands', 351)

g.insertar_arista('Centro Nacional de Artes Escénicas', 'Centro Nacional de Artes Escénicas', 135)
g.insertar_arista('Centro Nacional de Artes Escénicas', 'Burj al Arab', 1532)
g.insertar_arista('Centro Nacional de Artes Escénicas', 'Museo de Ciencias y Planetario de Nagoya', 153)
g.insertar_arista('Centro Nacional de Artes Escénicas', 'Edificio Cumulus', 4234)
g.insertar_arista('Centro Nacional de Artes Escénicas', 'El hotel Marina Bay Sands', 1325)

g.insertar_arista('Burj al Arab', 'Museo de Ciencias y Planetario de Nagoya', 352)
g.insertar_arista('Burj al Arab', 'Edificio Cumulus', 2532)
g.insertar_arista('Burj al Arab', 'El hotel Marina Bay Sands', 235)

g.insertar_arista('Museo de Ciencias y Planetario de Nagoya', 'Edificio Cumulus', 2532)
g.insertar_arista('Museo de Ciencias y Planetario de Nagoya', 'El hotel Marina Bay Sands', 252)

g.insertar_arista('Edificio Cumulus', 'El hotel Marina Bay Sands', 2352)



print('''
c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
''')

print('Arbol de expansion minima de las maravillas naturales:')

arbol_min = g.kruskal()
arbol_min = arbol_min[1].split('-')
#print(arbol_min)
peso_total = 0

for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print('peso total:',peso_total)


print()
print('Arbol de expansion minima de las maravillas arquitectonicas modernas:')

arbol_min = g.kruskal()
arbol_min = arbol_min[0].split('-')
#print(arbol_min)
peso_total = 0

for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print('peso total:',peso_total)

print('''
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
''')
paises = g.contar_maravillas2()
cont_paises_con_maravillas_arquitectónicas_y_naturales = 0
for pais in paises:
    #print(pais, paises[pais])
    if paises[pais]['natural'] >= 1 and paises[pais]['arquitectonica_moderna'] >= 1:
        cont_paises_con_maravillas_arquitectónicas_y_naturales+= 1
        print('El pais',pais,'tiene maravillas arquitectónicas y naturales')
        #pass
if cont_paises_con_maravillas_arquitectónicas_y_naturales >= 1:
    print('Hay paises que tienen maravillas arquitectónicas y naturales')
else:
    print('No hay paises que tengan maravillas arquitectónicas y naturales')


print('''
e. determinar si algún país tiene más de una maravilla del mismo tipo;
''')
paises
for pais in paises:
    #print(pais, paises[pais])
    if paises[pais]['natural'] > 1 or paises[pais]['arquitectonica_moderna'] > 1:
        cont_paises_con_maravillas_arquitectónicas_y_naturales+= 1
        print('El pais',pais,'tiene más de una maravilla del mismo tipo.')
        print(pais, paises[pais])
        print()
        #pass

print('''
f. deberá utilizar un grafo no dirigido.
''')