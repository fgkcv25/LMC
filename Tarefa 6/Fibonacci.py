# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:18:31 2019

@author: CLIENTE
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)