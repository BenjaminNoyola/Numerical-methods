#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema: Splines Cúbicos


import matplotlib.pyplot as plt
from numpy import *

n = int(raw_input("Escribe el número de puntos que contiene la lista: ")) 

#*********************Introducción de puntos x,y **********************#
coefX,coefY,i,LX_j = [],[],0,0
while(i < n):                                              
	X = float(raw_input("Ingresa el punto x_{0}: ".format(i))) 
	Y = float(raw_input("Ingresa el punto y_{0}: ".format(i)))  
	coefX.append(X)
	coefY.append(Y)                         
	if i==0:
		LI=X
	elif i==n-1:
		LD=X   
	i += 1

#print coefX, coefY	#Imprime los puntos X Y contenidos en las listas.

A = zeros([n-2,n-2])
b = zeros([n-2])
h = zeros([n-1])

#************valores de h = (Xi+1 - Xi)*********************************
for i in range(n-1):
	h[i]=coefX[i+1]-coefX[i]

print "h: ",h

#*************Construcción del sistema de ecuaciones********************
#Construcción de A
for i in range (n-2):  #Diagonal principal
	A[i][i]=2*(h[i]+h[i+1])
for i in range (n-3):  #Laterales
	A[i][i+1]=h[i+1]
for i in range (1,n-2):
	A[i][i-1]=h[i]

print "A: ",A	

#construcción de b
for i in range(n-2):
	b[i]=6.0*(((coefY[i+2]-coefY[i+1])/h[i+1])-((coefY[i+1]-coefY[i])/h[i]))
print "b: ",b		
		
#*****************Solución del sistema de ecuaciones********************
# Encontramos los coeficientes de la ecuación cúbica:
coef_cubica = linalg.solve(A,b)
print "\nCoeficientes de la ec cubica" , coef_cubica

#*************Construcción de las ecuaciones cúbicas********************
import sympy as sm

x = sm.Symbol('x')
fx = sm.zeros(n-1,1)  # Forma de crear arreglos del tipo de sympy


for i in range(n-1):
	if i == 0:
		fx[i]=sm.simplify( (coef_cubica[i]/(6.0*h[i]))*(x-coefX[i])**3 + (coefY[i]/h[i])*(coefX[i+1]-x) + ((coefY[i+1]/h[i])-(coef_cubica[i]*h[i])/6.0)*(x-coefX[i]) )
	elif i==n-2:
		fx[i]=sm.simplify( (coef_cubica[i-1]/(6.0*h[i]))*(coefX[i+1]-x)**3 + \
		((coefY[i]/h[i])-(coef_cubica[i-1]*h[i])/6.0)*(coefX[i+1]-x) + (coefY[i+1]/h[i])*(x-coefX[i]) )
	else:
		fx[i]=sm.simplify( (coef_cubica[i-1]/(6.0*h[i]))*(coefX[i+1]-x)**3 + (coef_cubica[i]/(6.0*h[i]))*(x-coefX[i])**3 + \
		((coefY[i]/h[i])-(coef_cubica[i-1]*h[i])/6.0)*(coefX[i+1]-x) + ((coefY[i+1]/h[i])-(coef_cubica[i]*h[i])/6.0)*(x-coefX[i]) )

print "\nfx: ",fx

#***********Selección de la ecuación interpolante***********************
interpol = float(raw_input("Introduce el valor de x que deseas interpolar: ")) 
for i in range(n):
	if (coefX[i] < interpol and interpol < coefX[i+1]):
		 Ecua_interpolante = fx[i]

Y = Ecua_interpolante.evalf(subs={x:interpol})
print "\nEl valor de Y buscado es: ",Y

#************Gráfico para cualquier número de n splines*****************

for i in range(n-1):
	f=sm.lambdify(x,fx[i],"numpy")  
	x = linspace(coefX[i],coefX[i+1],200) # Para graficar con matplotlib necesitamos que x sea una lista
	y=f(x) 
	if i%2 ==0:
		plt.plot(x,y, 'b',lw=3)
	else:
		plt.plot(x,y, 'r',lw=3)
	x = sm.Symbol('x')
plt.plot(coefX,coefY,'k8',ms=15, alpha=0.7, mfc='purple')	
plt.grid(color='y', alpha=0.5, linestyle='dashed', linewidth=1.6)
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title(u'Splines cúbicos')
plt.show()
