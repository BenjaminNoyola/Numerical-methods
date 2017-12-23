#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
#Tema 37: tiempo de cálculo

import time							#importan este paquete


T_inicio=time.time()				#toman el tiempo al inicio

for i in range (10000000):   		#Aqui va el cuerpo del código
	i=i+1  						    # Como la solución del sistema de ecuaciones....
	
T_fin=time.time()					#Toman el tiempo al final


print "Tiempo total de cálculo: ", (T_fin-T_inicio)   # La diferencia es el tiempo de cálculo
