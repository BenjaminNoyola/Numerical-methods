#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín Salomón Noyola García
# Tema7: Sentencias condicionales

edad = int(input("¿Cuántos años tienes? "))  #Se le pide la edad al usuario

if edad < 18 and edad >=0:      
    print "Eres menor de edad a tus ",edad," años"
    
elif edad < 0 or edad >= 145:
	print "imposible"

else:
	print "Eres mayor de edad a tus",edad, " años"

print "\n\t Salimos del condicional"
