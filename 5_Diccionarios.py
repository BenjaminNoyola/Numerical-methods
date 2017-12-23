#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín Salomón Noyola García
# Tema5: Diccionarios

d={'clave 1':[1,2,3],
	'clave 2':True,
	'clave 3': "tipo string",
	4:65.09849  #La clave también puede ser un entero como lo es el 4
	}

print type(d)
print d['clave 1']
print d[4],"\n"

d['clave 1']="cambiamos a un str"
print d['clave 1']
