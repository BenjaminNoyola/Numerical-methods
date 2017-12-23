#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema 23: Método de punto fijo

import numpy as np               # Se importan los paquetes numpy y matplotlib 
import matplotlib.pyplot as plt  # Recomendación: tener instalado Anaconda con python 2.7
from sympy import *

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
pInicial = float(raw_input("Punto inicial: "))  
tolerancia = 0.000001
punto,itera = 10.0,0

gx=apart(fx,x)

deri = diff(gx, x)
deriEvaluada = deri.evalf(subs={x:pInicial})
print deriEvaluada


if (abs(deriEvaluada))>1:
	print "Elige otro punto de inicio o de lo contrario la función no es posible encontrarla por este método"

	
def f(pInicial):
	fun = gx.evalf( subs={x:pInicial})
	return fun

print '{0}\t\t{1}\t\t{2}\t\t{3}'.format('Iteración','pInicial', 'Xi+1', 'Error abs')  
while (abs(pInicial-punto) >= tolerancia):
	punto = pInicial
	xi_m_1 =f(pInicial)
	print '{0}\t\t{1}\t\t{2}\t\t{3}' .format(itera,"%.4f" % pInicial, "%.5f" %xi_m_1, "%.5f" %(abs((xi_m_1)-(punto))))
	pInicial  = xi_m_1
	itera=itera+1
	if itera == 40:
		break
	
