#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 21: Derivadas

from sympy import *

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
pInicial = float(raw_input("Punto inicial: "))  
tolerancia = 0.000000001
punto,itera = 10.0,0

def f(parametro):
	fun = fx.evalf( subs={x:parametro})
	return fun

def derivada(pInicial,num_deriv=1):
	deri = diff(fx, x, num_deriv) # La derivada puede ser la primera o la segunda derivada
	deriEvaluada = deri.evalf(subs={x:pInicial})
	return deriEvaluada

xi_m_1 = 20.51  # Este valor es sólo para que entre al cíclo.
print '{0}\t\t{1}\t\t{2}\t\t{3}'.format('It','Xi', 'Xi+1', 'Error')  
while (abs(f(xi_m_1)) >= tolerancia):
	
	fxi = f(pInicial)
	deri_fxi_1 = derivada(pInicial,1)
	deri_fxi_2 = derivada(pInicial,2)
	punto = pInicial
	
	xi_m_1 = pInicial-(fxi*deri_fxi_1)/((deri_fxi_1)**2 - (fxi*deri_fxi_2)) #Esta es la única línea de código que evalua...
	
	print '{0}\t\t{1}\t\t{2}\t\t{3}' .format(itera,"%.4f" % pInicial, "%.5f" %xi_m_1, "%.8f" %(abs(f(xi_m_1))))
	pInicial  = xi_m_1
	
	itera=itera+1
	if (itera==20):
		print "Elige otro punto para lograr una mejor convergencia"
		break
