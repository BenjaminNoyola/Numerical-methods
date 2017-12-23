#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 20: Método de Newton Raphson

from sympy import *

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
pInicial = float(input("Punto inicial: "))  
tolerancia = 0.0000001
punto,itera,xi_m_1 = 10.0,0,20.2

def f(param):
	fun = fx.evalf( subs={x:param})
	return fun

def derivada(pInicial):
	deri = diff(fx, x)
	deriEvaluada = deri.evalf(subs={x:pInicial})
	return deriEvaluada


print '{0}\t\t{1}\t\t{2}\t\t{3}'.format('Itera','Xi', 'Xi+1', 'Error')  
while (abs(f(xi_m_1)) >= tolerancia):
	
	fxi = f(pInicial)
	deri_fxi = derivada(pInicial)
	punto = pInicial
	
	xi_m_1 = pInicial-(fxi)/(deri_fxi) #Esta es la única línea de código que evalua...
	
	print '{0}\t\t{1}\t\t{2}\t\t{3}' .format(itera,"%.4f" % pInicial, "%.5f" %xi_m_1, "%.8f" %f(xi_m_1))
	pInicial  = xi_m_1
	
	itera=itera+1
	if (itera==40):
		print "Elige otro punto para lograr una mejor convergencia"
		break

deriEvaluada3 = fx.evalf(subs={x:xi_m_1})
print "La función evaluada en el punto de la raiz es: ", deriEvaluada3
