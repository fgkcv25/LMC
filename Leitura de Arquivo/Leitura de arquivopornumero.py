# -*- coding: utf-8 -*-
"""
Created on Tue May 21 07:51:07 2019
@author: 05873472955
"""


import numpy as np

with open('C:\\Users\\CLIENTE\\Desktop\\Jogos, Filmes, Etc. v5\\Estudos 2.0\\LabMatComp\\Leitura de Arquivo\\A.txt') as arquivo:
    dados = arquivo.readlines()
    
dados.remove(dados[1001])
dados.remove(dados[1000])

A = []
for linha in dados:
    A.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
A = np.asarray(A, dtype=np.float64)


with open('C:\\Users\\CLIENTE\\Desktop\\Jogos, Filmes, Etc. v5\\Estudos 2.0\\LabMatComp\\Leitura de Arquivo\\B.txt') as arquivoB:
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
    
    
arquivoC = open('C:\\Users\\CLIENTE\\Desktop\\Jogos, Filmes, Etc. v5\\Estudos 2.0\\LabMatComp\\Leitura de Arquivo\\C.txt','w+')

(m,n) = A.shape
(p,q) = B.shape


import time
T = time.time()

for Ai in range(1):
    for Bi in range(p):
        for Aj in range(n):
            for Bj in range(q):
                arquivoC.write(str(A[Ai,Aj]*B[Bi,Bj]).replace('.0',' '))
        arquivoC.write('\n')
        print('se foi uma linha')


print(time.time()-T)
arquivoC.close()