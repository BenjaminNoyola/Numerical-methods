#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema: Método de la falsa posición

import numpy as np               # Se importan los paquetes numpy y matplotlib 
import matplotlib.pyplot as plt  # Recomendación: tener instalado Anaconda
import sys

#******Se solicitan los intervalos del dominio de la función***********#
print """La función que se desea modelar se debe escribir en 'fx' 
en el cuerpo del código (línea 20), tambien puedes editar el máximo de iteraciones"""                                                   
tolerancia, maximo_Itera= 0.000001, 50
iInicial = float(input("Intervalo inicial (a): "))      
iFinal = float(input("Intervalo final (b): "))   
#**********************************************************************#

#********En esta sección se debe introducir la función f(x)************#
def f(x):
#	fx=x**5+11*x**4+42*x**3+54*x**2-27*x-81
	fx = 3*x**3-9*x**2-4   # Edita la función que deseas modelar en esta línea
	return fx
#**********************************************************************#

#*definición de x en un dominio [iInicial, iFinal] y 'y' depende de x**#
x = np.linspace(iInicial, iFinal,200)
y=f(x)     # Se manda a llamar la función dada en la línea 21
#**********************************************************************#

#*********Visualizamos nuestra función con un gráfico******************#
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'nuestra función')
plt.plot(x, y, 'rx',lw=4)   # 'y' en los rángos indicados con linspace(frontera izq, frontera der, puntos)
plt.grid(True)
plt.grid(color='y', alpha=0.5, linestyle='solid', linewidth=2.0) # intentar con dashed o solid. cambiar el ancho de línea con linewith
plt.show()
#**********************************************************************#

#*****************Inicia algoritmo de falsa posición*******************#
if (((f(iInicial) >= 0) and (f(iFinal) >= 0)) or ((f(iInicial)<=0) and (f(iFinal)<=0))):  # En esta línea se manda a llamar la función f definida en la linea 17
	print "Corrige los límites porque no se cumple el teorema del valor intermedio"   # 
	sys.exit(1)
	
contador,xr=0,100.0
print '{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}'.format('Iteración','Inicial', 'Final', 'Resu', 'Error')  
while ((abs(f(xr)) >= tolerancia) and (contador < maximo_Itera)):
	xr=(f(iInicial)*iFinal-f(iFinal)*iInicial) / (f(iInicial)-f(iFinal))
#	xr=iFinal-((f(iFinal)*(iFinal-iInicial))/(f(iFinal)-f(iInicial)))
	
	if (f(iInicial) > 0):        # En esta línea se manda a llamar la función definida en la línea 17, se evalúa con el parametro iInicial (a)
		if (f(iInicial)*f(xr) > 0):  # En esta línea se evalúa la función f con los parámetros iInicial y Pmedio
			iInicial=xr
		else:
			iFinal=xr
	elif (f(iInicial) < 0):
		if (f(iInicial)*f(xr) > 0):
			iInicial=xr
		else:
			iFinal=xr
	else:
		print "Ya has encontrado la solución: ", iInicial, "Error = 0.0"
	print '{0}\t\t\t{1}\t\t{2}\t\t{3}\t\t{4}' .format(contador,"%.5f" % iInicial, "%.5f" %iFinal, "%.5f" %xr, "%.5f" %(abs(f(xr))) )
	contador=contador+1
#**********************************************************************#
