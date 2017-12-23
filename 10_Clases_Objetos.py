#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: MC. Benjamín S. Noyola García
# Tema 10: Clases y objetos

class Humano:
	def __init__(self,edad):        #Atributos (caracteristicas)
		self.edad=edad
	
	def gritar(self,mensaje):       #métodos (acciones)
		print mensaje

pedro=Humano(25)                    #Objeto pedro, utiliza la clase humano(plantilla)
raul=Humano(22)

print 'soy pedro y tengo ',pedro.edad
print 'soy Raul y tengo ',raul.edad

pedro.gritar('Hola')
raul.gritar('Hola pedro')
