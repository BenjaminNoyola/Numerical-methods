#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema 30: Método de solución de sistemas de ecuaciones LU (Basado en el algoritmo del Burden)

from numpy import *
from random import randint
import sys
#import pprint
#import scipy
#import scipy.linalg 

#.......Generar Aleatoriamente Matrices y vector solución (1)............#
n=int(raw_input("Introduce las filas de la matriz cuadrada A: "))
matA=zeros([n,n])
matL=zeros([n,n])
matU=zeros([n,n])
matR=zeros([n,n])
vec=zeros([n])
vecX=zeros([n])
vecY=zeros([n])

for f in range (n):
	for c in range(n):
		matA[f][c] = randint(2, 9)

for f in range (n):
	vec[f] = random.uniform(10, 15)

#..Evaluar si es posible solucionar dicho sistema de ecuaciones (3,4,6)..#
def f(l,u):
	lu=l*u
	return lu

#....................Encontrar L y U ....................................#
matL[0][0]=matA[0][0]            
matU[0][0]=1.0
#----------------------------------------#
if (f(matL[0][0],matU[0][0])==0):		### PASO 1 ###
	print "EL programa se indetermina y se cerrará..."
	sys.exit(1)
#----------------------------------------#
for j in xrange(1,n):  # En este caso python recorre la lista hasta n-1
	matU[0][j]=matA[0][j]/matL[0][0]   	### PASO 2 ###
	matL[j][0]=matA[j][0]/matU[0][0]

for i in range(1,n):					### PASO 3 ###
	matU[i][i]=1.
	for j in range(i,n):
		sumaU=0
		sumaL=0
		
		for k in range(i):				### PASO 5 ###
			sumaL=sumaL+matL[j][k]*matU[k][i]
		matL[j][i]=(1/matU[i][i])*(matA[j][i]-sumaL)
		
		for k in range(i):
			sumaU=sumaU+matL[i][k]*matU[k][j]
		matU[i][j]=(1/matL[i][i])*(matA[i][j]-sumaU)
#----------------------------------------#
	if (f(matL[i][i],matU[i][i])==0): 	### PASO 4 y 6 ###
		print "EL programa se indetermina y se cerrará..."
		sys.exit(1)
#----------------------------------------#
		
#for i in range(0,n):
	#for k in range(0,n):	
		#for j in range(0,n):
			#matR[i][k]=matR[i][k]+matL[i][j]*matU[j][k]
#print "multiplicación de matrices a pie",matR

#..................Encontrar el vector "y" (paso 8).............................#
vecY[0]=vec[0]/matL[0][0]			### PASO 8 ###
for i in range(1,n):
	sumaY=0
	for j in range(i):
		sumaY=sumaY+matL[i][j]*vecY[j]
	vecY[i]=(1/matL[i][i])*(vec[i]-sumaY)
		
#..............Encontrar el vector solución x (paso 8).........................#
vecX[n-1]=vecY[n-1]/matU[n-1][n-1]	### PASO 8 ###
for i in range(n-1,-1,-1):
	sumaX=0
	for j in range(i+1,n):
		sumaX=sumaX+matU[i][j]*vecX[j]
	vecX[i]=(1/matU[i][i])*(vecY[i]-sumaX)
	
#......................Imprimir L,U,x,y .................................#
print "Matriz A: ",matA
print "Matriz L: ",matL
print "Matriz U: ",matU
#print "Vector b: ",vec
#print "Vector Y: ",vecY
print "Vector X (solución a pié): ",vecX

x = linalg.solve(matA,vec)  #solución del sistema de ecuaciones utilizando numpy
print "Solucion numpy: ",x





# .......Algo para jugar...............#
#P, L, U = scipy.linalg.lu(matA)

#print "A:"
#pprint.pprint(matA)

#print "P:"
#pprint.pprint(P)

#print "L:"
#pprint.pprint(L)

#print "U:"
#pprint.pprint(U)
