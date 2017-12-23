#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema 28: Integración por la regla del trapecio introduciendo los puntos

from numpy import *
from sympy import *
import matplotlib.pyplot as plt

n = int(raw_input("Introduce el número de intervalos 'n' ")) 
x = Symbol('x')

#...................Introducción de puntos x,y ....................#
coeficientesX,coeficientesY,i,LX_j = [],[],0,0
while(i <= n):                                              
	X = float(raw_input("Ingresa el punto x_{0}: ".format(i))) 
	Y = float(raw_input("Ingresa el punto y_{0}: ".format(i)))  
	coeficientesX.append(X)
	coeficientesY.append(Y)                         
	if i==0:
		LI=X         #Límite izquierdo a
	elif i==n:
		LD=X   		 #Límite derecho b
	i += 1
# .................................................................#

#...............Integración por el Método del trapecio.............#
suma=0.0
for i in range(n+1):
	if i==0:
		suma=coeficientesY[i]
	elif i==n:
		suma=suma + coeficientesY[n]
	else:
		suma=suma+2.0*coeficientesY[i]

integra=((LD-LI)/(2*n))*suma
print "La integral por la regla del trapecio es = ",integra

#integral_2=integrate(4*x**3-10*x+10, (x, LI, LD))
#print "La integral evaluandola analíticamente es = ",integral_2

#Error_relativo_porcentual=(abs(integra-integral_2)/integral_2)*100
#print "\nError relativo porcentual: ",Error_relativo_porcentual
