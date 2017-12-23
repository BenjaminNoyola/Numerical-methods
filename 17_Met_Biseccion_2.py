#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 17: Método de la Bisección de raices de un polinomio de grado n.

from sympy import *
import numpy as np

x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") #3*x**3 - 9*x**2 - 4
iInicial = float(raw_input("Intervalo inicial: "))      
iFinal = float(raw_input("Intervalo final: "))  
ini,fin=iInicial,iFinal

#******EN esta función se evaúa pmedio, iInicial y iFinal**************# 
def f(param):                         # Lo que hace esta función es sustituir en param a los parámetros iInicial, iFinal y pmedio
	fun = fx.evalf( subs={x:param})   # que mas adelante se necesitan, se mandarán a llamar con la leyenda f(iInicial) o f(Pmedio)
	return fun						  # Sustituye an la función fx el párametro en lugar de x; ej: 3*x**3 - 9*x**2 - 4 --> 3(iInicial)**3 - 9*(iInicial)**2 - 4
#**********************************************************************#

#****************Inicia algoritmo del método de Bisección**************#
contador,tolerancia = 0,0.000001
print '{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}'.format('Iteración','Inicial', 'Final', 'Resultado', 'Error')  
while (abs(iFinal-iInicial) >= tolerancia):
	
	Pmedio=(iFinal+iInicial)/2.0
			 
	#.........................Se eligen los límites....................................#
	if (((f(iInicial) > 0) and (f(iFinal) > 0)) or ((f(iInicial)<0) and (f(iFinal)<0))):  # En esta línea se manda a llamar la función f definida en la linea 17
		print "Corrige los límites porque no se cumple el teorema del valor intermedio"   # 
		break
 	else:
		if (f(iInicial) > 0):        # En esta línea se manda a llamar la función definida en la línea 17, se evalúa con el parametro iInicial (a)
			if (f(iInicial)*f(Pmedio) > 0):  # En esta línea se evalúa la función f con los parámetros iInicial y Pmedio
				iInicial=Pmedio
			else:
				iFinal=Pmedio
		elif (f(iInicial) < 0):
			if (f(iInicial)*f(Pmedio) > 0):
				iInicial=Pmedio
			else:
				iFinal=Pmedio
		else:
			print "Ya has encontrado la solución: ", iInicial, "Error = 0.0"
	 
	print '{0}\t\t\t{1}\t\t{2}\t\t{3}\t\t{4}' .format(contador,"%.5f" % iInicial, "%.5f" %iFinal, "%.5f" %((iFinal+iInicial)/2), "%.5f" %(abs((iFinal)-(iInicial))) )
	contador=contador+1
#**********************************************************************#

#****Encontrar la raiz del polinomio utilizando herramientas de numpy**#
coeff = [3, -9, 0, -4]
print "Las raices del polinomio '3*x**3 - 9*x**2 - 4' encontradas con numpy",np.roots(coeff)
#**********************************************************************#

#**Inicia gráfico de la función a la cual se le encontó la raiz********#
p = plot(fx,(x, ini, fin), title=u"Gráfico",xlabel="x",ylabel="y", show=False) #la u sirve para poner acentos en el título
p[0].line_color = 'blue'
p.show()
#**********************************************************************#
