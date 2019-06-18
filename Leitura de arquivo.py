# -*- coding: utf-8 -*-
"""
Created on Tue May 21 07:51:07 2019

@author: 05873472955
"""


import numpy as np

with open('C:\\Users\\05873472955\\Desktop\\A.txt') as arquivo:
    dados = arquivo.readlines()
    
dados.remove(dados[1001])
dados.remove(dados[1000])

matriz = []
for linha in dados:
    matriz.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
matriz = np.asarray(matriz, dtype=np.float64)


with open('C:\\Users\\05873472955\\Desktop\\B.txt') as arquivoB:
    dadosB = arquivoB.readlines()
    
dadosB.remove(dadosB[1507])
dadosB.remove(dadosB[1506])
dadosB.remove(dadosB[1505])
dadosB.remove(dadosB[1504])

matrizB = []
for linha in dadosB:
    matrizB.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
i = 0
while i < len(matrizB):
    if len(matrizB[i]) != 1000:
        matrizB.pop(i)
    else:
        i = i+1
    
matrizB = np.asarray(matrizB, dtype=np.float64)
    
    
def Kron(A,B):
    (m,n) = A.shape
    (p,q) = B.shape
    
    C = np.zeros((m*p,n*q))
    
    for Ai in range(m):
        for Bi in range(p):
            for Aj in range(n):
                for Bj in range(q):
                    C[Ai*p+Bi,Aj*q+Bj] = A[Ai,Aj]*B[Bi,Bj]

s = ''
s.join('')