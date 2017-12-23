#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín Salomón Noyola García
# Tema8: Bucles

#Bucle infinito
#~ i=0
#~ while (i >= 0):
	#~ print "Hola enfermera",i
	#~ i=i+1

#~ tabla=input("¿que tabla de multiplicación desea imprimir? ")
#~ i=0
#~ while (i < 10):
	#~ print tabla," X ",i," = ",tabla*i 
	#~ i=i+1


tabla=input("¿que tabla de multiplicación desea imprimir? ")
i=0
while (i <= 10):
	print tabla," X ",i," = ",tabla*i 
	if i==5:        
		break       #Rompe el ciclo aunque no se halla cumplido la condición
	i=i+1


#lista=range(0,11)
#print type(lista),lista

#lista2=range(0,11,2)
#print lista2


#tabla=int(input("¿que tabla de multiplicación desea imprimir? "))
#for i in range(0,11):
	#print tabla," X ",i," = ",tabla*i 
