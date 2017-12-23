#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Autor: Benjamín Noyola
# Tema EU: Integración por la regla de Simpson introduciendo los puntos

import numpy as np
from sympy import *

h = float(raw_input("Introduce el paso 'h:' ")) 
a = float(raw_input("Introduce el dominio, punto 'a' ")) 
b = float(raw_input("Introduce el dominio, punto 'b' ")) 
#xc = float(raw_input("Introduce la condición inicial de x ")) 
yc = float(raw_input("Introduce la condición inicial de y ")) 
Particiones=(b-a)/h

def f(punto):
	fun = fx.evalf( subs={x:punto})
	return fun

if b<a:
	print "Corrige los límites del dominio"

x = Symbol('x')
fx = input("Introduce el lado derecho de la ecuación diferencial:") 

vecx = np.linspace(a, b,Particiones+1)
vecy=np.zeros([Particiones+1])

vecy[0]=yc
vecy[1]=yc+h*f(a)

j,k=int(Particiones),h
for i in xrange(2,j+1):
	vecy[i]=2.0*h*f(a+k)+vecy[i-1]
	k=k+h

print vecx,vecy

import matplotlib.pyplot as plt

plt.plot(vecx, vecy, 'r',lw=4)   # 'y' en los rángos indicados con linspace(frontera izq, frontera der, puntos)
plt.grid(True)
plt.grid(color='b', alpha=0.5, linestyle='solid', linewidth=1.0) # intentar con dashed o solid. cambiar el ancho de línea con linewith
plt.show()

n = np.linspace(0.0, 4.0, 200)
m=-(0.5*n**4) + 4*n**3 -10*n**2 +8.5*n
plt.plot(n, m, 'r',lw=4)   # 'y' en los rángos indicados con linspace(frontera izq, frontera der, puntos)
plt.grid(True)
plt.grid(color='b', alpha=0.5, linestyle='solid', linewidth=1.0) # intentar con dashed o solid. cambiar el ancho de línea con linewith
plt.show()


