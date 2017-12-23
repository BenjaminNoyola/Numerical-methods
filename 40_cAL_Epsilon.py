#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema Cálculo de epsilon máquima, mantisa y digitos significativos
import numpy as np

#***********Cálculo encontrando el epsilon y la mantisa ***************#
eeps=1
yy=2
t=0
while (yy > 1.0):
	eeps=eeps/2.0
	yy=1.0+eeps
	t=t+1.0

print "Epsilon = ", (eeps), "\n Mantisa = ",(t)
print "Base en hexadecimal = ",float.hex(eeps)


#****Cálculo encontrando el epsilon y la mantisa con Double************#
print "-----------Double-------------------"
eepsilonD=1
eepsilonD=np.longdouble(eepsilonD)
yyD=2
t=0
while (yyD > 1.0):
	eepsilonD=eepsilonD/2.0
	yyD=1.0+eepsilonD
	t=t+1.0

print "Epsilon Double= ", (eepsilonD), "\n Mantisa = ",(t)


#****Herramientas de python epsilon************#
import sys
print "Epsilos con herramientas de python: ",sys.float_info.epsilon
print "número de digitos significativos en python: ",sys.float_info.dig
print "Mantisa con herramientas de python: ",sys.float_info.mant_dig
