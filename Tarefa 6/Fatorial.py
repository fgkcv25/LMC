# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:16:13 2019

@author: CLIENTE
"""

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)