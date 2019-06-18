# -*- coding: utf-8 -*-
"""
Spyder Editor

Este programa fatora a matriz A em sua forma PLU.
"""

import numpy as np
import copy
import time

t0 = time.time()

A = np.random.rand(int(100*np.random.rand()),int(1000*np.random.rand()))
(m,n) = np.shape(A)
#eu fiz isso para transformar a matriz numa matriz de floats, para a divisão funcionar
#e nomeei as matrizes U, L e P, pois o código as transformará nas PLU da fatoração LU de A
U = copy.deepcopy(A) + np.zeros((m,n))
L = np.identity(m)
P = np.identity(m)


pivo = 0
while pivo < min(n,m):
    #aqui o programa checa se precisa fazer uma troca de linhas ou não
    if U[pivo,pivo] != 0:
        #aí caso não precise, o programa transformará ambas a L e a U para que
        #se tornem nas matrizes desejadas da fatoração LU, com a U sendo transformada
        #diretamente, com multiplicação por escalar e soma de linhas, para que
        #todos os elementos abaixo do pivô atual se tornem 0, 
        #e a L sendo transformada pela multiplicação do inverso das matrizes elementares
        #que fizeram a transformação na U, por isto crio uma Lreserva,
        #que é tal transformação inversa, que logo depois transformará a L na
        #multiplicação L@Lreserva, isto se repetindo em todos os passos da transformação de U.
        Lreserva = np.identity(m)
        Lreserva[pivo,:] = Lreserva[pivo,:]*U[pivo,pivo]
        U[pivo,:] = U[pivo,:]/U[pivo,pivo]
        L = np.dot(L,Lreserva)
        for i in range(pivo+1,m):
            Lreserva = np.identity(m)
            Lreserva[i,:] = Lreserva[i,:] + Lreserva[pivo,:]*U[i,pivo]
            U[i,:] = U[i,:] - U[pivo,:]*U[i,pivo]
            L = np.dot(L,Lreserva)
        pivo = pivo + 1
    else:
        #só que se precisar de uma troca de linhas para poder se ter um pivõ
        #não-nulo para transformar os elementos abaixo dele em 0,
        #o programa passa por este passo para trocar as linhas da U, procurando
        #a primeira linha com elemento abaixo do pivô não nulo para isto, e trocando
        #ela com a linha do pivô, fazendo a mesma coisa também com a matriz P,
        #para que ela se torne a matriz de permutação de linhas da fatoração LU
        for i in range(pivo,m):
            if U[i,pivo] != 0:
                Uguardar = copy.deepcopy(U[pivo,:])
                U[pivo,:] = U[i,:]
                U[i,:] = Uguardar
                Pguardar = copy.deepcopy(P[pivo,:])
                P[pivo,:] = P[i,:]
                P[i,:] = Pguardar
                break
            else:
                #também, caso a coluna seja completamente nula,
                #criei este else para evitar um loop infinito e simplesmente
                #passar para a próxima coluna
                if i == m-1:
                    pivo = pivo+1
                    break

print(np.allclose(P@L@U,A))
print(time.time() - t0)