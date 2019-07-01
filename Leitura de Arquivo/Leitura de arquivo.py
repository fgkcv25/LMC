# -*- coding: utf-8 -*-
"""
Created on Tue May 21 07:51:07 2019

@author: 05873472955
"""


import numpy as np

with open('C:\\Users\\05873472955\\Desktop\\LEitura de Arquivo\\A.txt') as arquivo:
    dados = arquivo.readlines()
    
dados.remove(dados[1001])
dados.remove(dados[1000])

A = []
for linha in dados:
    A.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
A = np.asarray(A, dtype=np.float64)


with open('C:\\Users\\05873472955\\Desktop\\LEitura de Arquivo\\B.txt') as arquivoB:
    dadosB = arquivoB.readlines()
    
dadosB.remove(dadosB[1507])
dadosB.remove(dadosB[1506])
dadosB.remove(dadosB[1505])
dadosB.remove(dadosB[1504])

B = []
for linha in dadosB:
    B.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
i = 0
while i < len(B):
    if len(B[i]) != 1000:
        B.pop(i)
    else:
        i = i+1
    
B = np.asarray(B, dtype=np.float64)
    
    
arquivoC = open('C:\\Users\\05873472955\\Desktop\\LEitura de Arquivo\\C.txt','w+')
(m,n) = A.shape
(p,q) = B.shape


listadematrizes = [1*B,2*B,3*B,4*B,5*B,6*B,7*B,8*B,9*B,10*B]
    
for Ai in range(m):
    C = []
    for Aj in range(n):
        C.append(listadematrizes[int(A[Ai][Aj])-1])
    for i in range(len(C)):
        C[i] = list(C[i])
    C = str(C)
    C = C.rstrip(']').replace(']','\n').replace('.0','').replace(',','').replace('[','')
    arquivoC.write(C)
    
arquivoC.close()


    
 
