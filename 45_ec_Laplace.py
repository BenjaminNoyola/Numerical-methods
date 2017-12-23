#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: BENJAMÍN S. NOYOLA GARCÍA
# Tema solución de la ecuación de Laplace con diferencias finitas.

import matplotlib.pyplot as plt
from numpy import *


lx=float(input("Tamaño del dominio en x: "))
ly = float(input("Tamaño del dominio en y: "))
partx = int(input("Particiones del dominio en x: "))
party = int(input("Particiones del dominio en y: "))
cn = int(input("Condición de frontera norte: "))
cs = int(input("Condición de frontera sur: "))
ce = int(input("Condición de frontera este: "))
co = int(input("Condición de frontera oeste: "))

delx=lx/partx+1
dely=ly/party+1
a=1/delx
b=1/dely
c=(a+b)

matA=zeros([partx*party,partx*party])
matsol=zeros([party+2,partx+2])
vecb=zeros([partx*party])

for i in range(partx*party):
	matA[i][i]=-2*c

for i in range(partx*party-1):
	matA[i+1][i]=a
	matA[i][i+1]=a

i=partx-1
while i < (partx*party-1): 
	matA[i+1][i]=0
	matA[i][i+1]=0
	i=i+partx

i=0
while i < (partx*party-partx): 
	matA[i+partx][i]=b
	matA[i][i+partx]=b
	i=i+1


print matA

for i in range(partx):
	vecb[i]=-b*cs
	if (i == 0):
		vecb[i]=vecb[i]-a*co
	elif (i==partx-1):
		vecb[i]=vecb[i]-a*ce

for i in range(partx*party-partx,partx*party):
	vecb[i]=-b*cn
	if (i == partx*party-partx):
		vecb[i]=vecb[i]-a*co
	elif (i==partx*party-1):
		vecb[i]=vecb[i]-a*ce

i=partx
while (i <= partx*party-2*partx):
	vecb[i]=-a*co
	i=i+partx
	
i=2*partx-1
while (i <= partx*party-partx-1):
	vecb[i]=-a*ce
	i=i+partx

x = linalg.solve(matA,vecb)
#print "x",x
#print vecb

k=0
for i in range(1,party+1):
	for j in range(1,partx+1):
		matsol[i][j]=x[k]
		k=k+1

for i in range(partx+2):
	matsol[0][i]=cs
for i in range(partx+2):
	matsol[party+1][i]=cn	

for i in range(party+2):
	matsol[i][0]=co
for i in range(party+2):
	matsol[i][party+1]=ce


#Aquí graficamos el contorno de Isotermas; Esta es la solución contenida en forma matricial 
#en el archivo de texto importado anteriormente y guardado en "data".

fig = plt.figure(1) 
plt.title('Contorno de Isotermas')
plt.xlabel('Y')
plt.ylabel('X')
cs1 = plt.contourf((matsol), 100) # Pintamos 100 niveles con relleno
plt.colorbar()
plt.show()


