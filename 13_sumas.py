#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín S. Noyola García
# Tema 13: Ejemplo suma: cálculo de la varianza y desviación estandar y 
#          lectura de archivos de texto


#................... Lectura de archivo txt en columna..................#
archivo=open('personas.txt','r') 
datos=archivo.readlines()
#datos=archivo.read()
archivo.close()
#.......................Fin de Lectura de archivo txt..................#


print type(datos)  # Sirve para saber de que tipo de variabler se trata                       
#print int(datos[2][0])+int(datos[2][0])   #convierte str a int


#.....................Cálculo de la media aritmética....................#
j,num,suma=0,0,0
for i in range(0,4):              #Calculo de la suma para encontrar la media
	j=j+float(datos[i][0])
	num=num+1

media=j/num                        #Cálculo de la media
print "media: ",media

#.....................Cálculo de la varianza....................#
for i in range(0,4):                #Calculo de la suma para encontrar la varianza
	suma=suma+(float(datos[i][0]) - media)**2

varianza=suma/num

#.....................Impresión de resultados....................#
print "Varianza: ",varianza          
print 'desv estandar: ', (varianza)**0.5
