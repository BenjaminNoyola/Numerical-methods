# -*- coding: utf-8 -*-
#! /usr/bin/env python


import matplotlib.pyplot as plt
import sys
from numpy import *
import time

lx = float(raw_input('\nDefine la longitud de x: '))
ly = float(raw_input('\nDefine la longitud de y: '))
nx = int(raw_input('\nDefine el numero de particiones en x: '))
ny = int(raw_input('\nDefine el numero de particiones en y: '))
CO = float(raw_input('\nCondicion Oeste: ')) #Limite derecho del intervalo
CE = float(raw_input('\nCondicion Este: '))    
CN = float(raw_input('\nCondicion Norte: '))
CS = float(raw_input('\nCondicion Sur: '))
deltax = lx/(nx + 1)       #Tamaño de cada recuadro de la malla en x.
deltay = ly/(ny + 1)

#Resolviendo numéricamente por diferencias finitas, creamos los espacios para matrices y vectores:
mA = zeros([nx*ny,nx*ny])     
matsol=zeros([ny+2,nx+2])      
vb = zeros(nx*ny)               
a = 1.0/(deltax**2)      
b = 1.0/(deltay**2)
c = a + b       

# Entradas de la matriz A 
for j in range (nx*ny):          
	mA[j][j] = -2*c
for j in range (nx*ny-1):
    mA[j+1][j] = a
    mA[j][j+1] = a
    
j= nx-1
while (j<nx*ny-1):
	mA[j+1][j]=0
	mA[j][j+1]=0
	j=j + nx

for j in range (nx*ny-nx):
	mA[j][j+nx] =b
	mA[j+nx][j]= b

print mA	
# Entradas del vector b

for j in range (nx):
	vb[j]= -b*CS
	if j==0:
		vb[j]= vb[j]-a*CO
	elif j==nx-1:
		vb[j]= vb[j]-a*CE

for j in range (nx*ny-nx,nx*ny):
	vb[j]= -b*CN
	if j==nx*ny-nx:
		vb[j]= vb[j]-a*CO
	elif j==nx*ny-1:
		vb[j]= vb[j]-a*CE


for j in range (nx,nx*ny-2*nx+1,nx):
	vb[j]= -a*CO

for j in range (2*nx-1,nx*ny-nx,nx):
	vb[j]= -a*CE

sol = linalg.solve(mA,vb) 

print sol


k=0
for i in range(1,ny+1):
	for j in range(1,nx+1):
		matsol[i][j]=sol[k]
		k=k+1

for i in range(nx+2):
	matsol[0][i]=CS
for i in range(nx+2):
	matsol[ny+1][i]=CN	

for i in range(ny+2):
	matsol[i][0]=CO
for i in range(ny+2):
	matsol[i][nx+1]=CE

print matsol
#

fig = plt.figure(1) 
plt.title('Contorno de Isotermas')
plt.xlabel('Y')
plt.ylabel('X')
cs1 = plt.contourf((matsol), 300) # Pintamos 100 niveles con relleno
plt.colorbar()
plt.show()
# Listo :P
