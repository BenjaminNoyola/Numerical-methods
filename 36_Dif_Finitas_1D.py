#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín S. Noyola García
#Tema 36: Método de diferencias finitas, solución de una ec. dif. ordinaria en 1D:
#  -u''(x) + u'(x) + u(x) = f
#  f = (pi^2+1)*e^x*sen(pi*x) − pi*e^x*cos(%pi*x)
#  la solución es: u(x) = e^x sen(pi x)

import numpy as np 
from sympy import *
import matplotlib.pyplot as plt

# .......Número de Particiones y tamaño de paso.............#
n = int(raw_input("Introduce el número de particiones del dominio: "))  
Li,Ld = 0.5,(3.0/2.0)   #Límite izquierdo y derecho
h=(Ld-Li)/(n+1)         #Tamaño de paso necesario para evaluar diferencias finitas centrales.

# ..................Solución analítica.............#
u=np.zeros(n+2)
x=np.linspace(Li, Ld, n+2) 		#Dominio de la solución analítica
j=Li
for i in range(n+2):			#Solución analítica
	u[i]=np.exp(j)*np.sin(np.pi*j)
	j=j+h	
#print u        

# .............Inicia solución numérica..............#
matA=np.zeros([n,n])            # Espacio de la matriz
vecb=np.zeros(n)				# Espacio del vector b 
a=(-1.0/(h**2)+1.0/(2*h))	    # constantes encontradas en la discretización con diferencias finitas centrales
b=(2.0/(h**2)+1)
c=(1.0/(h**2)+1.0/(2*h))

for i in range (1,n-1):         #Creación de la matriz que se resuelve
	matA[i][i]=b				# Este ciclo se crea a partir del patron de la solución con diferencias finitas
	matA[i][i+1]=a             
	matA[i][i-1]=-c
matA[0][0]=b					
matA[0][1]=a
matA[n-1][n-2]=-c
matA[n-1][n-1]=b

j=Li+2.*h
for i in range(1,n):			# llenado del vector b
	vecb[i]=(np.pi**2+1.0)*np.exp(j)*np.sin(j*np.pi)-np.pi*np.exp(j)*np.cos(j*np.pi)
	j=j+h

vecb[0] = (np.pi**2+1.)*np.exp(Li+h)*np.sin((Li+h)*np.pi)-np.pi*np.exp(Li+h)*np.cos((Li+h)*np.pi)+c*np.exp(Li) # Primer valor del vector b
vecb[n-1]=(np.pi**2+1.)*np.exp(Ld-h)*np.sin((Ld-h)*np.pi)-np.pi*np.exp(Ld-h)*np.cos((Ld-h)*np.pi)+a*np.exp(Ld) # último valor del vector b

#print matA
#print vecb

sol = np.linalg.solve(matA,vecb)  #solución del sistema de ecuaciones utilizando numpy
#print "Solucion numpy: ",x

sol=np.insert(sol,0,np.exp(Li))	#Se inserta el valor de la condicion de frontera izquierda
sol=np.append(sol,-np.exp(Ld))	#Se inserta el valor de la condicion de frontera derecha
Error = abs(abs(sol-u)/u)*100					#Se encuentra el error absoluto entre la solución numérica y analítica
#print "La solución numérica es: ",x

# ................Gráficos de solución analítica, solución numérica y error....................#

#plt.xlabel('x')       # Gráfico de solución analítica
#plt.ylabel('y')
#plt.title(u'Solución analítica')
#plt.plot(x, u, '-o')
#plt.grid(color='y', alpha=0.5, linestyle='dashed', linewidth=1.6)
#plt.show()

#plt.xlabel('x')       # Gráfico de solución numérica
#plt.ylabel('y')
#plt.title(u'Solución numérica')
#plt.plot(x,sol, '-o')
#plt.grid(color='b', alpha=0.5, linestyle='solid', linewidth=1.6)
#plt.show()

#**********************************
ax = plt.subplot(2, 1, 1)	# Esta es la etiqueta del gráfico 1
plt.xlabel('x')				# Se coloca nombre al eje x		
plt.ylabel('y')				# Se coloca nombre al eje y
plt.title(u'Solución analítica')     # Se coloca nombre al grafico
plt.plot(x, u, '-o',lw=2, color="red")
plt.grid(color='y', alpha=0.5, linestyle='dashed', linewidth=1.6)                  

#......... Aqui comienza el segundo gráfico.................
ax = plt.subplot(2, 1, 2)	# Esta es la etiqueta del gráfico 2
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'Solución numérica')
plt.plot(x,sol, '-o')
plt.grid(color='b', alpha=0.5, linestyle='solid', linewidth=1.6)

plt.show()				#Muestra el gráfico completo.
#**********************************

plt.xlabel('x')       # Gráfico del Error punto a punto
plt.ylabel('y')
plt.title(u'Error (Analítiva vs Numérica)')
plt.plot(x, Error, '-o')
plt.grid(color='g', alpha=0.5, linestyle='dashed', linewidth=1.6)
plt.show()
