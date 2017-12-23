#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín Noyola García
# Tema9: Funciones


#def mi_funcion(num1,num2):
#	print num1+num2

#mi_funcion(6.0,4)




#def f(x, y):
 #   return x **2, y **2

#a, b = f(2, 3)
#print a,b



#def sumar(x=0, y=0):
#    return x + y

#print sumar(4,5)



def mi_funcion(cadena,v=1,*algomas):
	print cadena*v
	for i in algomas:	
		print i*v

mi_funcion("python\t",3,'hola\t','enfermera\t','adios\t','clase\t')
