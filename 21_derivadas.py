#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema 21: Derivadas

from sympy import *  # Sugerencia: Tener instalado Anaconda

x = Symbol('x')

fx = raw_input("Introduce una funcion donde x es la variable independiente: ")  #Para introducir "3x" debes escribir 3*x, de lo contrario=error

deri = diff(fx, x)
deri2 =diff(fx, x,2)
print "El polinomio derivado, respecto a x es: ", deri

deriEvaluada = deri.evalf( subs={x:3})
print "La derivada evaluada en el punto x es: ", deriEvaluada

deri = diff(fx, x)
print "La segunda derivada respecto a x es: ", deri2

deriEvaluada2 = deri2.evalf( subs={x:3})
print "La segunda derivada evaluada en el punto x es: ", deriEvaluada2
