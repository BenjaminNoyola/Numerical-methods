#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema 28: Integración por la regla del trapecio introduciendo una función

from numpy import *
from sympy import *
import matplotlib.pyplot as plt

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
n = int(raw_input("introduce el número de intervalos 'n' en los que deseas particionar la función: "))
LI = float(raw_input("introduce el límite izquierdo de la función: "))
LD = float(raw_input("introduce el límite derecho de la función: ")) 

def f(punto):
	fun = fx.evalf( subs={x:punto})
	return fun

pmedio=LI+(LD-LI)/n
#...............Integración por el Método del trapecio.............#
suma=0.0
for i in range(n+1):
	if i==0:
		suma=f(LI)
	elif i==n:
		suma=suma + f(LD)
	else:
		suma=suma + 2.0*f(pmedio)
		pmedio=pmedio + (LD-LI)/n

integra=((LD-LI)/(2*n))*suma
print "La integral por la regla del trapecio es = ",integra

integral_2=integrate(fx, (x, LI, LD))
print "La integral evaluandola analíticamente es = ",integral_2

Error_relativo_porcentual=(abs(integra-integral_2)/integral_2)*100
print "\nError relativo porcentual: ",Error_relativo_porcentual
