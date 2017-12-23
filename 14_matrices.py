#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín S. Noyola García
# Tema 14: creacion de una matriz y escritura de archivos de texto

#..................Solicitar al usuario numero de filas y columnas...................#
matriz=[]
filas=int(raw_input("Cantidad de filas: "))
columnas = int(raw_input("Cantidad de columnas: "))


#..................Creación de una matriz (A pie)...................#
for i in range (filas):
	matriz.append([0]*columnas)

print "Matriz (append): ", matriz

for f in range (filas):
	for c in range(columnas):
		matriz[f][c] = int(raw_input("Elemento %d,%d : "% (f,c)))

print "Matriz (append): ", matriz


#...................creacion de una matriz utilizando numpy..................#
from numpy import *
matA=zeros([filas,columnas])

print "Matriz (numpy): ", matA

for f in range (filas):
	for c in range(columnas):
		matA[f][c] = int(raw_input("ElementoNP %d,%d : "% (f,c)))

print "Matriz (numpy): ", matA



