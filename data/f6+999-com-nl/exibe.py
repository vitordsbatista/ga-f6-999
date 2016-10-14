#!/usr/bin/python
# -*- coding: utf-8 -*-
#===================================#
# File name: 						#
# Author: Vitor dos Santos Batista	#
# Date created: 					#
# Date last modified: 				#
# Python Version: 2.7				#
#===================================#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


arq = 'f6+999-com-NL-'
tipoB = 'best-'
tipoM = 'mean-'
tipoW = 'worst-'

best = np.zeros((1, 201))[:-1]
mean = np.zeros((1, 201))[:-1]
worst = np.zeros((1, 201))[:-1]

for i in range(10):
    a = np.load(arq+tipoB+'%i.npy' %(i))
    best = np.vstack((best, a))
    a = np.load(arq+tipoM+'%i.npy' %(i))
    mean = np.vstack((mean, a))
    a = np.load(arq+tipoW+'%i.npy' %(i))
    worst = np.vstack((worst, a))

plt.yticks(np.arange(999, 1000, .1))
a = np.mean(best, 0)
b = np.mean(mean, 0)
c = np.mean(worst, 0)
plt.plot(a, label = 'Melhor')
plt.plot(b, label = 'Medio')
plt.plot(c, label = 'Pior')
plt.legend(loc=5)
plt.show()
