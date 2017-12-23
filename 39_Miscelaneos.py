#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema: Cálculo de derivadas, integrales, raices, raices múltipples, series, 
		#generación de números aleatorios, productos matriciales y vectoriales,
		#Solucion de sistemas de ecuaciones lineales.

#Este código sirve para mostrar las herramientas de python + (numpy, sympy)
#Los estudiantes podrán comparar sus resultados de los métodos numéricos 
#con los resultados de numpy, sympy con los alias np, sm respectivamente.	

import sympy as sm
import numpy as np
from random import randint

x, y= sm.symbols("x, y")  # Antes de comenzar, se declaran simbolos x, y

#**********************Derivadas e integrales**************************# 
#print """------------1-------------"""
#y=(x + sm.pi)**2
#print sm.diff(y, x)

#print """------------2-------------"""
#y = sm.sin(3*x**2)-6*x**6
#deri= sm.diff(y, x)                 #Método para derivar
#print deri

#print """------------2*-------------"""
#y = sm.sin(3*x**2)-6*x**6
#deri2= sm.diff(y, x, 2)                 #Método para encontrar la segunda derivada (fun,variable,#derivada)
#print "Segunda derivada",deri2

#print """------------3-------------"""
#y = sm.sin(3*x**2)-6*x**6
#deri= sm.diff(y, x)     
#print sm.integrate(deri, x)         #Método para integrar deri, nos regresa 'y'

#print """------------4-------------"""
#f=x**3 + 6.0 * x**2 + 11.0*x + 6.0
#print sm.integrate(f, (x,1,2))		#Método para integrales definidas

#print """------------5-------------"""
#print sm.integrate(sm.exp(-x**2), (x, -sm.oo, sm.oo)) #Método para integrales impropias
##http://nbviewer.ipython.org/github/franktoffel/UA-MIMAT/blob/f364d833d9059247f75e91dcfb2cc2c5bf7b07c8/Introduccion-a-Sympy.ipynb
##**********************************************************************#

##***************Raices, raices múltiples y expansión en series*********#
#print """------------6-------------"""
#a=sm.solve(x**2-x,x)
#print a			#Regresa las raices de la expresión: x**2-x donde x es la var_indep

#print """------------7-------------"""
#expr=x**3-6*x**2+9*x
#b=sm.solve(expr,x)  #la expresión puede introducirse en el resolvedor
#print b				#Solo regresa las raices

#print """------------8-------------"""
#c=sm.roots(expr,x) #Encuentra las raices y aparte especifica si hay multiplicidad de raices
#print c				#{3: 2, 0: 1}  dos raices con valor de 3 y 1 raiz con valor cero.

#print """------------9-------------"""
#serie = sm.series(sm.exp(x), x)  
##serie = sm.series(sm.sin(x),x)
##serie=(sm.exp(x), x, 1, 10) #Por defecto se expande la expresión de alrededor de x=0, pero podemos expandir en torno a cualquier valor de x incluyendo explícitamente un valor en la llamada a la función:
#print "la expansión en series de potencias de exp(x) es: ",serie

#----------------------------------------------------------------------
#http://docs.sympy.org/latest/tutorial/calculus.html#finite-differences
#**********************************************************************#

##*******números aleatorios, producto de matrices, solución de SEL******#
#a= randint(2,9)   # Genera números aleatorios enteros entre 2 y 9, sujetos a modificaciones
#b= np.random.random() # Genera números aleatorios flotantes entre 0 y 1
#c=np.random.uniform(2, 9) #Genera números aleatorios flotantes entre 2 y 9, sujetos a modificaciones
#print """-----------10-------------"""
#print a
#print b
#print c
#print """....... Creación de las matrices utilizando Random ............."""
#filasA=int(raw_input("Cantidad de filas de A: "))
#columnasA = int(raw_input("Cantidad de columnas de A: "))
#columnasB = int(raw_input("Cantidad de columnas de B: "))

#matA=np.zeros([filasA,columnasA])
#matB=np.zeros([columnasA,columnasB])
#matR=np.zeros([filasA,columnasB])

#for f in range (filasA):
	#for c in range(columnasA):
		#matA[f][c] = randint(2,9)
	

#for f in range (columnasA):
	#for c in range(columnasB):
		#matB[f][c] = randint(10,19)

##print "Matriz A", matA
##print "Matriz B", matB

#print """-----------11-------------"""
## Para multiplicar matrices utilizando numpy solo se escribe:
#print "multiplicación de matrices usando numpy", np.dot(matA,matB)



