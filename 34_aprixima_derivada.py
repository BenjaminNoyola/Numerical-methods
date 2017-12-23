#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema 34: Aproximación a la derivada utilizando diferencias finitas hacia atrás, adelante y centrales.

from sympy import *


x = Symbol('x')
fx = input("Introduce una funcion donde x es la variable independiente: ") 
h = float(input("introduce la magnitud del paso h: "))  
punto = float(input("introduce el punto donde se desea evaluar la función: "))  



def adelante(punto,h):
	fx_eval = fx.evalf(subs={x:punto})
	fxi_ade_eval=fx.evalf(subs={x:punto+h})
	deri_adelante=(fxi_ade_eval-fx_eval)/(h)
	return deri_adelante
	
def atras(punto,h):
	fx_eval = fx.evalf(subs={x:punto})
	fxi_atras_eval=fx.evalf(subs={x:punto-h})
	deri_atras=(fx_eval-fxi_atras_eval)/(h)
	return deri_atras

def centrales(punto,h):
	fx_atras_eval = fx.evalf(subs={x:punto-h})
	fxi_ade_eval=fx.evalf(subs={x:punto+h})
	deri_central=(fxi_ade_eval-fx_atras_eval)/(2*h)
	return deri_central

def analitica(punto, fx):
	analitica=diff(fx, x)
	R_eval = analitica.evalf(subs={x:punto})
	print "La derivada analítica es: ",R_eval
	return R_eval

print """\nElije el tipo de primera derivada que deseas evaluar:
1.- Aproximación de la primera derivada hacia adelante
2.- Aproximación de la primera derivada hacia atras
3.- Aproximación de la primera derivada centrales"""

i = int(raw_input("\n"))  

if i==1:
	print "La derivada es: ",adelante(punto,h)
	A=analitica(punto,fx)
	Error_porcentual=abs(adelante(punto,h)-A)/A*100
	print "El error porcentual encontrado es: ",Error_porcentual
elif i==2:
	print "La derivada es: ",atras(punto,h)
	A=analitica(punto,fx)
	Error_porcentual=abs(atras(punto,h)-A)/A*100
	print "El error porcentual encontrado es: ",Error_porcentual
elif i==3:
	print "La derivada es: ",centrales(punto,h)
	A=analitica(punto,fx)
	Error_porcentual=abs(centrales(punto,h)-A)/A*100
	print "El error porcentual encontrado es: ",Error_porcentual
else:
	print "el número que introdujiste no es correcto"
