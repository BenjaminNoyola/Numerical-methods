#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Método de Gauss-Seidel para resolver sistemas de ecuaciones

from numpy import *

#****Generar los espacios de matrices y vectores****
n = int(raw_input("Por favor introduce el numero de filas/columnas:"))
A = zeros([n,n])
b = zeros([n])
X = zeros([n])
X0 = zeros([n])

print "Introduce las entradas de la matriz A: "
for i in range(0,n):
	for j in range(n):
		A[i][j] = int(raw_input("Entrada %d,%d : "%(i+1,j+1)))

print "Introduce las entradas del vector b: "		
for i in range(0,n):
	b[i] = int(raw_input("Entrada %d: "% (i+1)))
	
print "Matriz A: \n", A
print "Vector b: \n", b

#****Solución con el algoritmo de G-S***
tolerancia,norma,contador = 0.000001,1,0
while(norma>tolerancia):
	for i in range(0,n):
		suma = 0
		for j in range(0,n):
			if(j<i):
				suma = suma - A[i][j]*X[j]
			elif(j>i):
				suma = suma - A[i][j]*X0[j]
			else:
				suma = suma + 0
		X[i] = (b[i]+suma)/A[i][i]
	contador = contador+1
	print " Iteracion ", contador, X 
	norma = linalg.norm(X-X0)
	for i in range(0,n):
		X0[i] = X[i]

#...___Solucion X comparación usando NUMPY___...
resultado = linalg.solve(A,b)
print "Comparando con la solucion que da NUMPY: \n" , resultado
