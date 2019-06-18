# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:57:24 2019

@author: 05873472955
"""
import numpy as np
with open('C:\\Users\\05873472955\\Desktop\\B.txt') as arquivoB:
    dadosB = arquivoB.readlines()
    
dadosB.remove(dadosB[1507])
dadosB.remove(dadosB[1506])
dadosB.remove(dadosB[1505])
dadosB.remove(dadosB[1504])

matrizB = []
for linha in dadosB:
    matrizB.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
matrizB = np.asarray(matrizB, dtype=np.float64)
    