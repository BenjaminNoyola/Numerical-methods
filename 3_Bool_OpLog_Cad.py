#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema3: Cadenas, Booleanos y Op lógicos


#comillas simples
cadenaS = 'Texto entre comillas \n simples\n'  # \n: caracter de escape

#comillas dobles
cadenaD="\tcomillas dobles"  #\t sirve para hacer una tabulación

#comilllas triples
cadenota = '''\nlinea1
\tLinea2
linea3 '''

print type(cadenaS),cadenaS
print cadenaD
print cadenota

#Repeticion y concatenación
hi="Hola\t"*2
print hi

cad1='Hola'
cad2=" enfermera"

print cad1+cad2, "\n\n"    #concatenación


#Booleanos
logAnd= True and False and True #Si alguno es falso, el resultado es falso
logOr = False or False or True  #Si alguno es verdadero, el resultado es verdadero
logNot= not False               #Invierte el resultado

print logAnd
print logOr
print logNot
