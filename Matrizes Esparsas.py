# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:40:29 2019

@author: 05873472955
"""

import numpy as np
A = np.array([[0,0,0,0,71,5,0,0],[0,1,2,0,40,10,0,0],[0,0,0,0,0,0,0,0],[0,0,1,2,4,0,0,0],[0,0,0,1,0,0,0,1],
              [1,0,5,320,10,3,0,0],[5,1,6,0,0,0,0,0],[0,10,0,0,0,0,0,0]])
B = np.random.rand(8,8)

(n,m) = A.shape
(p,q) = B.shape
(rows,cols) = A.nonzero()

C = np.zeros((n,q))

for i in range(n):
    for j in range(q):
        for ak in range(rows.size):
            if i == rows[ak]:
                C[i,j] = C[i,j]+A[i,cols[ak]]*B[cols[ak],j]
                        
                        
print(C)
print(np.allclose(C,A@B))