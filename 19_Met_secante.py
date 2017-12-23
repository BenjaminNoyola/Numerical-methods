#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 16: Método de la secante

import numpy as np               # Se importan los paquetes numpy y matplotlib 
import matplotlib.pyplot as plt  # Recomendación: tener instalado Anaconda

print """La función que se desea modelar se debe escribir en 'fx' 
en el cuerpo del código (línea 18)"""                                                   
tolerancia = 0.000001
iInicial = float(raw_input("Intervalo inicial: "))      
iFinal = float(raw_input("Intervalo final: "))   

def f(x):
	fx = x**5+11*x**4+42*x**3+54*x**2-27*x-81 #4np.exp(-x)-x # Edita la ecuación que deseas modelar en esta línea
	return fx

x = np.linspace(iInicial, iFinal,200)
y=f(x)

itera=0
print '{0}\t{1}\t\t{2}\t\t{3}\t\t{4}'.format('Iteración','X_i-1', 'X_i', 'X_i+1', 'Error abs')  
while (abs(iFinal-iInicial) >= tolerancia):
	fxi_1 = f(iInicial)
	fxi   = f(iFinal)
	
	xi_m_1 = iFinal-(fxi*(iInicial-iFinal))/(fxi_1 - fxi) #Esta es la única línea de código que evalua la ec de la secante.
	
	print '{0}\t\t{1}\t\t{2}\t\t{3},\t\t{4}' .format(itera,"%.4f" % iInicial, "%.5f" %iFinal, "%.5f" %(xi_m_1), "%.5f" %(abs((xi_m_1)-(iInicial))))
	iInicial= iFinal
	iFinal  = xi_m_1
	itera=itera+1
