#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S Noyola García
# Tema 15: Multiplicación de matrices

from numpy import *
from random import randint

#a= randint(2,9)   #
b= random.random() #
#c=random.uniform(2, 9) #
#print a
print b
#print c
#....... Creación de las matrices utilizando Random .............
filasA=int(raw_input("Cantidad de filas de A: "))
columnasA = int(raw_input("Cantidad de columnas de A: "))
columnasB = int(raw_input("Cantidad de columnas de B: "))

matA=zeros([filasA,columnasA])
matB=zeros([columnasA,columnasB])
matR=zeros([filasA,columnasB])

for f in range (filasA):
	for c in range(columnasA):
		matA[f][c] = randint(2,9)
	

for f in range (columnasA):
	for c in range(columnasB):
		matB[f][c] = randint(10,19)

print matA
print matB

# Aquí comienza la  multiplicación de matrices utilizando el algoritmo 
# del producto interior
print matR
for i in range(0,filasA):
	for k in range(0,columnasB):	
		for j in range(0,columnasA):
			matR[i][k]=matR[i][k]+matA[i][j]*matB[j][k]
print "multiplicación de matrices a pie",matR

# Para multiplicar matrices utilizando numpy solo se escribe:
print "multiplicación de matrices usando numpy", dot(matA,matB)
