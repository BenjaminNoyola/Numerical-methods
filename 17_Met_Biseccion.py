#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 17: Método de la Bisección de raices de un polinomio de grado n.

import numpy as np               # Se importan los paquetes numpy y matplotlib 
import matplotlib.pyplot as plt  # Recomendación: tener instalado Anaconda

tolerancia = 0.000001
grado = int(raw_input("Grado de ecuacion: "))                                                    
iInicial = float(raw_input("Intervalo inicial: "))      
iFinal = float(raw_input("Intervalo final: "))     

#...................Introducción de coeficientes........................#
coeficientes,potencias,i,contador = [],[],grado,0
while(i >= 0):                                              
	cof = float(raw_input("Ingresa x^{0}: ".format(i)))     
	coeficientes.append(cof)
	potencias.append(i)                           
	i -= 1

#...........................Bisección...................................#
print '{0}\t\t\t{1}\t\t\t{2}\t\t{3}'.format('Iteración','Inicial', 'Final', 'Resultado', 'Error')  
while (abs(iFinal-iInicial) >= tolerancia):
	x = np.linspace(iInicial, iFinal,60)  # Se crea una lista linspace(frontera izq, frontera der, puntos)
	
	Pmedio=(iFinal+iInicial)/2.0
	Fi,Ff,Fm,y=0,0,0,0
	for i in xrange(0,grado+1):
		y=y+coeficientes[i]*(x**potencias[i])
		Fi = Fi+coeficientes[i]*(iInicial**potencias[i])
		Ff = Ff+coeficientes[i]*(iFinal**potencias[i])
		Fm = Fm+coeficientes[i]*(Pmedio**potencias[i])
	
	##.........................Gráficos......................................#
	#plt.title('Polinomio')
	#plt.plot(x, y, 'g.-')  # Esta línea de código sirve para indicar que se graficará y el formato
	#plt.xlabel('x')		 # En esta línea se coloca nombre al eje x
	#plt.ylabel('y')
	#plt.show()			 

	#.........................Se eligen los límites....................................#
	if ((Fi>0) and (Ff>0)) or ((Fi<0) and (Ff<0)):
		print "Corrige los límites porque no se cumple el teorema del valor intermedio"
		break
 	else:
		if (Fi > 0):
			if (Fi*Fm > 0):
				iInicial=Pmedio
			else:
				iFinal=Pmedio
		elif (Fi < 0):
			if (Fi*Fm > 0):
				iInicial=Pmedio
			else:
				iFinal=Pmedio
		else:
			print "Ya has encontrado la solución: ", iInicial, "Error = 0.0"
	 
	print '{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}' .format(contador,"%.5f" % iInicial, "%.5f" %iFinal, "%.5f" %((iFinal+iInicial)/2), "%.5f" %(abs((iFinal)-(iInicial))) )
	contador=contador+1
