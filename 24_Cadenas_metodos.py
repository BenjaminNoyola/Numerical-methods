#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema 24: Cadenas y sus métodos


s= "Hola mundo"  	# Es una cadena

print len(s) 		# mide numero de carácteres de la cadena

# Uso del método count
print s.count("a",0,5)		# s.count(valor, inicio, fin)  cuenta el numero de veces que se repite la cadena
print s.count("l") 			# Reconoce mayusculas y minusculas
print s.count("o",0,len(s))


#  Método Cambio de mayúsculas y minúsculas
print s.lower() # cambia a munúsculas
print s.upper() # cambia a minúsculas


#  Método para remplazar una cadena
print s.replace("o","XX",2) # cadena.replace(valor,nuevo,repeticiones(Ocurrencias))
print s.replace("o","XX",1)

#método para separar split
print s.split("a")				# s.split(separador, maxsplit)
print s.split("o",2)			# Sirve para limitar el numero de veces qu se va a cortar la cadena
print s.split()                 # Separa la cadena unicamente con espacios

# método para buscar
print s
print s.find("o",2,10) 					#s.find(valor, inicio, fin)
print s.find("l") 	

