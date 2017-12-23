#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema4: Listas (arreglos) y tuplas

#En una misma lista se pueden colocar diferentes tipos de datos
l=["cero",1,2.566,['otra lista',True],159,35]  
print type(l)

l2=l[0]
l3=l[3][0]        #comienza a contar la lista de la posición cero
l4=l[0:3]         #A partir de la posición 0, se extraen 3 elementos
l5=l[0:3:2]       #Extrae Uno si y uno no.
l6=l[1::2]        #Extrae Uno si y uno no, de toda la lista.
l7=l[-1]          #Comienza a contar de -1 de atrás para adelante, intentar  l7=l[-1::-1], l7=l[-1::-2]
l8=l[:3]		  #Se extraen 3 elementos a partir de la posición 0,  l8=l[3:]

print "l",l
#print "l2: ",l2
#print "l3: ",l3
#print "l4: ",l4
#print "l5: ",l5
#print "l6: ",l6
#print "l7: ",l7
#print "l8: ",l8,"\n\n"

l[0:2]=[0,"uno"] #Se modifican 2 valores a partir de la posición cero
print "l",l

l[0:2]=[]
#print "\n",l,"\n"


#Tuplas, son de dimensión fija, no se puedes modificar
t=("cero",1,2.566)
#print type(t)
#print t[0]   # Se puede acceder a la posición cero de la tupla como en las listas
