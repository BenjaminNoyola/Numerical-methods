#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema 29: Integración por la regla de Simpson introduciendo los puntos

from numpy import *
from sympy import *

n = int(raw_input("Introduce el número 'par' de intervalos 'n' ")) 
if n%2!=0:
	print "Esta evaluación no funcionará porque n no es par."
x = Symbol('x')

#...................Introducción de puntos x,y ....................#
coeficientesX,coeficientesY,i,LX_j = [],[],0,0
while(i <= n):                                              
	X = float(raw_input("Ingresa el punto x_{0}: ".format(i))) 
	Y = float(raw_input("Ingresa el punto y_{0}: ".format(i)))  
	coeficientesX.append(X)
	coeficientesY.append(Y)                         
	if i==0:
		LI=X         #Límite izquierdo a (inferior)
	elif i==n:
		LD=X   		 #Límite derecho b  (Superior)
	i += 1
# .................................................................#

#...............Integración por el Método de SIMPSON 1/3.............#
suma=0.0
for i in range(n+1):
	if i==0:
		suma=coeficientesY[i]
	elif i==n:
		suma=suma + coeficientesY[n]
	else:
		if i%2==0:
			suma=suma + 2.0*coeficientesY[i]
		else:
			suma=suma + 4.0*coeficientesY[i]

integra=((LD-LI)/(3*n))*suma
print "La integral por la regla de Simpson 1/3 es = ",integra

