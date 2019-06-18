# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:48:59 2019

@author: 05873472955
"""

import matplotlib.pyplot as plt
import numpy as np
import math

m = 10
x = np.arange(-10.,10.,0.2)
y = [np.cos(i) for i in x]
z = np.arange(-10.,10.,0.2)

for xizinho in range(x.size):
    zezinho = 0
    for i in range(m):
        zlinha = ((-1)**(2*i))*x[xizinho]**(2*i)/math.factorial(i)
        zezinho = zlinha + zezinho
    z[xizinho] = zezinho

fig, axes = plt.subplots()
axes.plot(x,y,'m',linewidth=10)
axes.plot(x,z,'g',linewidth=10)
axes.axis([-10,10,-10,10])
plt.xlabel('sei lá')
plt.ylabel('show')
plt.title('ok')



#figure = janela de fora
#axes = janela de dentro
#axis = vc sabe
