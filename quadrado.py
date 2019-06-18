# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:12:26 2019

@author: 05873472955
"""

import numpy as np

def bi(f,a,b,tolerancia=1e-10):
    if f(a)*f(b) > 0:
        print('não tenho o que fazer com isto')
    elif np.abs(f(a)) < tolerancia:
        return a
    elif np.abs(f(b)) < tolerancia:
        return b
    else:
        x = (a+b)/2
        niter = 0
        while np.abs(f(x)) > tolerancia:
            if f(x)*f(a) < 0:
                b = x
            else:
                a = x
            x = (a+b)/2
            niter = niter+1
        return x, niter
    
    
    
def n(x):
    if n == 0:
        return 1
    else:
        k = 1
        while x != 1:
            k = k*x
            x = x-1
        return k
    

#ou
        
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        n = n*fatorial(n-1)
    return n