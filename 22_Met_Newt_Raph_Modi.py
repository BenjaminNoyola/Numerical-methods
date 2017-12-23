#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 21: Derivadas

from sympy import *

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
pInicial = float(raw_input("Punto inicial: "))  
tolerancia = 0.0000001
punto,itera = 10.0,0

def f():
	fun = fx.evalf( subs={x:pInicial})
	return fun

def derivada(pInicial,num_deriv=1):
	deri = diff(fx, x, num_deriv) # La derivada puede ser la primera o la segunda derivada
	deriEvaluada = deri.evalf(subs={x:pInicial})
	return deriEvaluada


print '{0}\t\t{1}\t\t{2}\t\t{3}'.format('It','pInicial', 'Xi+1', 'Error abs')  
while (abs(pInicial-punto) >= tolerancia):
	
	fxi = f()
	deri_fxi_1 = derivada(pInicial,1)
	deri_fxi_2 = derivada(pInicial,2)
	punto = pInicial
	
	xi_m_1 = pInicial-(fxi*deri_fxi_1)/((deri_fxi_1)**2 - (fxi*deri_fxi_2)) #Esta es la única línea de código que evalua...
	
	print '{0}\t\t{1}\t\t{2}\t\t{3}' .format(itera,"%.4f" % pInicial, "%.5f" %xi_m_1, "%.5f" %(abs((xi_m_1)-(punto))))
	pInicial  = xi_m_1
	
	itera=itera+1
	if (itera==40):
		print "Elige otro punto para lograr una mejor convergencia"
		break
