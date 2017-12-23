#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Benjamín Noyola García
# Tema 26: Interpolación de Lagrange

import numpy as np 
from sympy import *
from sympy.abc import x
import matplotlib.pyplot as plt

grado = int(raw_input("Grado de la interpolación deseada: ")) 
x = Symbol('x')

#...................Introducción de puntos x,y ....................#
coeficientesX,coeficientesY,i,LX_j = [],[],0,0
while(i <= grado):                                              
	X = float(raw_input("Ingresa el punto x_{0}: ".format(i))) 
	Y = float(raw_input("Ingresa el punto y_{0}: ".format(i)))  
	coeficientesX.append(X)
	coeficientesY.append(Y)                         
	if i==0:
		LI=X
	elif i==grado:
		LD=X   
	i += 1

print coeficientesX, coeficientesY	#Imprime los puntos contenidos en las listas.

#***************Construcción del polinomio de Lagrange******************
for j in range (0,grado+1):     #Este ciclo sirve para construir el polinomio de 							Lagrange
	i,lj=0,1
	while (i <= grado):
		if (i==j):
			i=j+1
			if i==grado+1:
				break
#		print i
		lj=lj*((x-coeficientesX[i])/(coeficientesX[j]-coeficientesX[i]))
		i=i+1
	LX_j=LX_j+coeficientesY[j]*lj	#resultado sin simplificar de la suma de y_j 							l_j(x) (Polinomio de lagrange)

plt.plot(coeficientesX, coeficientesY, 'go')	#Este gráfico es generado con el 									módulo matplotlib
plt.show()
Lx_j=simplify(LX_j)
print "El polinomio de Lagrange es: ", Lx_j   #Simplifica e imprime la 											expresión de L(x)

#**********Evaluación del punto X en el polinomio de Lagrange***********
p_eval = float(raw_input("Introduce un valor de x donde deseas evaluar el polinomio 	de Lagrange: "))
Y = LX_j.evalf(subs={x:p_eval})
print "El valor de Y es con X dado es: ", Y

#p2 = plot(LX_j,(x,LI,LD))           #Este gráfico es generado con el módulo sympy

f=lambdify(x,Lx_j,"numpy")
x = np.linspace(LI,LD,200)
y=f(x)
 
plt.plot(x,y,coeficientesX, coeficientesY ,"ro")
plt.show()
