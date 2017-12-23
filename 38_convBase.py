#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Noyola García
# Tema: Cambio de decimal a binario y viceversa 

#**** Conversión de decimal a binario (a pie)**************************#
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))

#**********************************************************************#
print """ \n Otra manera de convertir de decimal a binario 
utilizando las herramientas de python: """

print"en binario es: ", bin(numero)       
b= int(bin(numero)[2:]) # nos regresa solo la parte entera del binario
print"el entero b: ", b

print '''\n Convertir de binario a decimal utilizando las 
herramientas de python (convierte el binario almacenado en la variable b)'''
print int(str(b), 2)


#*****************************importante*******************************#
print"\n\n operación importante", 5173.0//12.0 # entrega solo la parte entera de la división, aunque la entrega como flotante
print 5173.0/12.0

#**************** Cambio de decimal a cualquier base ******************#

#def cambio_base(decimal, base):
    #conversion = ''
    #while decimal // base != 0:
        #conversion = str(decimal % base) + conversion
        #decimal = decimal // base
    #return str(decimal) + conversion

#numero = int(input('Introduce el número a cambiar de base: '))
#base = int(input('Introduce la base: '))
#print(cambio_base(numero, base))

