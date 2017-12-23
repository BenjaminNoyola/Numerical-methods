#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 20: Método de Newton Raphson

import numpy as np               # Se importan los paquetes numpy y matplotlib 
import matplotlib.pyplot as plt  # Recomendación: tener instalado Anaconda
from sympy import *

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
pInicial = float(raw_input("Punto inicial: "))  
tolerancia = 0.000001
punto,itera = 10.0,0

def f():
	fun = fx.evalf( subs={x:pInicial})
	return fun

def derivada(pInicial):
	deri = diff(fx, x)
	deriEvaluada = deri.evalf(subs={x:pInicial})
	return deriEvaluada


print '{0}\t\t{1}\t\t{2}\t\t{3}'.format('Iteración','pInicial', 'Xi+1', 'Error abs')  
while (abs(pInicial-punto) >= tolerancia):
	
	fxi = f()
	deri_fxi = derivada(pInicial)
	punto = pInicial
	
	xi_m_1 = pInicial-(fxi)/(deri_fxi) #Esta es la única línea de código que evalua...
	
	print '{0}\t\t{1}\t\t{2}\t\t{3}' .format(itera,"%.4f" % pInicial, "%.5f" %xi_m_1, "%.5f" %(abs((xi_m_1)-(punto))))
	pInicial  = xi_m_1
	
	itera=itera+1
	if (itera==40):
		print "Elige otro punto para lograr una mejor convergencia"
		break

deriEvaluada3 = fx.evalf(subs={x:xi_m_1})
print "La función evaluada en el punto de la raiz es: ", deriEvaluada3
