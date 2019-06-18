# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:44:18 2019

@author: 05873472955
"""

A = [[1,2],[2,1]]
M = copy.deepcopy(A) #ou usa copy.deepcopy(A)
I = []

for i in range(len(M)):
    miniI = []
    for j in range(len(M)):
        if i == j:
            miniI.append(1)
        else:
            miniI.append(0)
    I.append(miniI)
L = []
P = []

i = 0
while i < min(len(M),len(M[1])):
    if M[i][i] != 0:
        Pivô = M[i][i]
        for jlinha in range(len(M[1])):
            M[i][jlinha] = M[i][jlinha]/Pivô
        for jlinha in range(len(I)):
            I[i][jlinha] = I[i][jlinha]*Pivô
        print(I)
        for linhas in range(i+1,len(M)):
           minipivô = M[linhas][i]
           for colunasdalinha in range(len(M[1])):
               M[linhas][colunasdalinha]=M[linhas][colunasdalinha]-minipivô*M[i][colunasdalinha]
           for colunasdalinha in range(len(I)):
               I[linhas][colunasdalinha]=I[linhas][colunasdalinha]+minipivô*I[i][colunasdalinha]
        print(I)
        i = i+1
    else:
        teste = 0
        while teste < len(M):
            if M[teste][i] != 0:
                replace = M[i]
                M[i] = M[teste]
                M[teste] = replace
                teste = len(M)
            else:
                teste = teste+1
                if teste == len(M):
                    print('ABORTAR MISSÃO')
                    i = min(len(M),len(M[1]))
                    
                    
                    
print(M)


