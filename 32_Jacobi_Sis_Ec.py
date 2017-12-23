#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema 32: Método de solución de sistemas de ecuaciones Jacobi(Basado en el algoritmo de Burden)

from numpy import *
import sys

#.......Generar Aleatoriamente Matrices y vector solución (1)............#
n=int(input("Introduce en número de filas de la matriz cuadrada A: "))
matA=zeros([n,n])
inv_matD=zeros([n,n])
matR=zeros([n,n])   # Equivalemte a L+U
vecR2=zeros([n])
vecR3=zeros([n])
vecb=zeros([n])
vecx=zeros([n])
vecxAnt=ones([n])

for f in range (n):
	for c in range(n):
		matA[f][c] = int(raw_input("Elemento %d,%d : "% (f,c)))

for f in range (n):
	vecb[f] = int(raw_input("Elemento %d: "% (f)))

print "Matriz A: \n",matA
print "Vector b: \n",vecb

#Construcción de la matriz D inversa
for i in range(n):
	for j in range(n):
		inv_matD[i][i]=1./matA[i][i]
			
#Construcción de la matriz R
for i in range(n):
	for j in range(n):
		if (i!=j):
			matR[i][j]=matA[i][j] # Se construye a partir de los coeficientes de A pero sin los coeficientes.


print "Matriz D inversa",inv_matD
print "Matriz R",matR

norma,tol=2,0.00001

while norma>tol:
	vecR2=dot(matR,vecxAnt)
	vecR3=vecb-vecR2
	vecx=dot(inv_matD,vecR3)
#	print vecx
	norma=linalg.norm(vecx-vecxAnt)
	vecxAnt=vecx

print "Vector X: ",vecx

x = linalg.solve(matA,vecb)  #solución del sistema de ecuaciones utilizando numpy
print "Solucion numpy: ",x
