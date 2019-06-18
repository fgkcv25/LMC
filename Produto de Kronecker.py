# -*- coding: utf-8 -*-
"""
Este código calcula o produto de Kronecker
"""

import numpy as np
import time

t0 = time.time()

A = np.random.rand(int(100*np.random.rand()),int(100*np.random.rand()))
B = np.random.rand(int(100*np.random.rand()),int(100*np.random.rand()))

(m,n) = A.shape
(p,q) = B.shape

C = np.zeros((m*p,n*q))

for Ai in range(m):
    for Bi in range(p):
        for Aj in range(n):
            for Bj in range(q):
                C[Ai*p+Bi,Aj*q+Bj] = A[Ai,Aj]*B[Bi,Bj]
                
                
print(time.time()-t0)
print(np.allclose(np.kron(A,B),C))
print(time.time()-t0)
print(C.shape)
