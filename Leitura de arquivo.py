# -*- coding: utf-8 -*-
"""
Created on Tue May 21 07:51:07 2019

@author: 05873472955
"""


import numpy as np

with open('C:\\Users\\CLIENTE\\Desktop\\Jogos, Filmes, Etc. v5\\Estudos 2.0\\LabMatComp\A.txt') as arquivo:
    dados = arquivo.readlines()
    
dados.remove(dados[1001])
dados.remove(dados[1000])

A = []
for linha in dados:
    A.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
A = np.asarray(A, dtype=np.float64)


with open('C:\\Users\\CLIENTE\\Desktop\\Jogos, Filmes, Etc. v5\\Estudos 2.0\\LabMatComp\B.txt') as arquivoB:
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
    
    
def Kron(A,B):
    (m,n) = A.shape
    (p,q) = B.shape
    
    C = np.zeros((m*p,n*q))
    
    for Ai in range(m):
        for Bi in range(p):
            for Aj in range(n):
                for Bj in range(q):
                    C[Ai*p+Bi,Aj*q+Bj] = A[Ai,Aj]*B[Bi,Bj]
    return C

C = Kron(A,B)


s = list(C)
for i in range(len(s)):
    s[i] = list(s[i])
s = str(s)
s = s.rstrip(']').replace(']','\n').replace('.0','').replace(',','').replace('[','')

arquivoC = open('C:\\Users\\CLIENTE\\Desktop\\Jogos, Filmes, Etc. v5\\Estudos 2.0\\LabMatComp\C.txt','w+')
arquivoC.write(s)
arquivoC.close()