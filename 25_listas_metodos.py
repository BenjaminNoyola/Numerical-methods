#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema 25: Listas y sus métodos

#...........Definición de las listas.....................#
lista1=[1,"Dos",3.0,"Dos"]
print "Lista 1: ",lista1

lista2=range(0,11)
print "Lista 2: ",lista2

#..........¿Se encuentra el elemento en la lista?..............#
print ".........................1.........................\n"
dato=1

print dato in lista1     #Es como una pregunta ¿Esta dato en lista1?
print "1" in lista1 	 #False
print 1 in lista1


#.............Encontrar la posición del valor en la lista...........# 
print ".........................2.........................\n"
print lista1.index(3.0)
print lista2.index(6)

dato2=100
#Evitar el error
if dato2 in lista1:
	print lista1.index(dato2)
else:
	print "El dato no se encuentra en la lista"

#............Agregar elementos a la lista.....................#
print ".........................3.........................\n"
lista2.append(100)
print lista2

#..........Contar elementos repetidos en una lista............#
print ".........................4.........................\n"
print lista1.count("Dos")

#.........Insertar un dato en una posición específica de una lista.......#
print ".........................5.........................\n"
print lista2
lista2.insert(5,"Cinco")
print lista2

#........Transforma una lista (La modifica) acoplando una nueva lista........#
print ".........................6.........................\n"
lista3 = range(1,6,2)
print "lista3: ",lista3

iterable=range(0,6,2)
#iterable="cadena"
lista3.extend(iterable)

print "lista3: ",lista3

#.........Método pop sirve para sacar un elemento de una lista y borrarlo......# 
print ".........................7.........................\n"
# Se reacomoda la lista para q no queden huecos.
lista3.pop()  		#lista.pop(indice), si no se le coloca indice extrae el úntimo  
print "lista 3 despúes de aplicar pop",lista3
print lista3.pop(2) # Extrae y borra el dato de acuerdo al indice
print "lista 3: ",lista3        #Lista 3 despues de aplicar pop(2) 

#........ Metodo para remover un elemento de la lista (Elimina el primero que se encuentra)......#
print ".........................8.........................\n"
lista3.remove(0)       # Para eliminar todos los elementos que contengan el dos, 
print lista3			#se hace un ciclo for
lista3.append(3)
print lista3
for i in lista3:
	lista3.remove(3)

print lista3

#Invertir el orden de una lista 

lista3.reverse()
print lista3			#también cambian los indices


# ............Eliminar una fila o columna de una matriz.........................#
print ".........................9.........................\n"
import numpy

x = numpy.array([[1,2,3],
				 [4,5,6],
				 [7,8,9]])

x = numpy.delete(x, (0), axis=0)  #axis 0 se refiere a la fila
x = numpy.delete(x,(2), axis=1)	  #axis 1 se refiere a la columna

print x
