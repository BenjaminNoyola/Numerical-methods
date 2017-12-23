#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Benjamín.
# Tema: Formación de un polinomio de grado n

from numpy import *
from sympy import *
import matplotlib.pyplot as plt

grado = int(raw_input("Grado del polinomio: ")) 
x = Symbol('x')

#...................Introducción de coeficientes del polinomio ....................#
i,pol = grado,0
while(i >= 0):  #comenzamos del coeficiende de variable con mas alto grado
	coef = float(raw_input("Ingresa el coeficiente de x**{0}: ".format(i))) 
	pol = pol+coef*x**i # En esta líne se concatena el polinomio
	i -= 1   #disminuye de uno en uno
	
print "El polinimio será: ", pol     # Imprime el polinomio 
print "Factorización del polinomio", factor(pol)    # Factoriza el polinomio con la herramienta "factor" de sympy"
