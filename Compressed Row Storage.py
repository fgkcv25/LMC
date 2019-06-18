# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:56:55 2019

@author: 05873472955
"""

import numpy as np

M = np.array([[0,0,0,0,71,5,0,0],[0,1,2,0,40,10,0,0],[0,0,0,0,0,0,0,0],[0,0,1,2,4,0,0,0],[0,0,0,1,0,0,0,1],
              [1,0,5,320,10,3,0,0],[5,1,6,0,0,0,0,0],[0,10,0,0,0,0,0,0]])
B = np.random.rand(8,8)

(n,m) = M.shape
(p,q) = B.shape

A = []
IA = [0]
JA = []
ia = 0
C = np.zeros((n,q))

for i in range(n):
    iareserva = 0
    for j in range(m):
        if M[i,j] != 0:
            A.append(M[i,j])
            JA.append(j)
            iareserva = iareserva+1
    ia = ia + iareserva
    IA.append(ia)
    
    
for i in range(n):
    for j in range(q):
        for ii in range(len(IA)-1):
            for jj in JA[IA[i]:IA[i+1]]:
                C[i,j] = C[i,j]+M[i,jj]*B[jj,j]
                
print(np.allclose(C,M@B))