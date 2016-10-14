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


arq = 'f6-sem-NL-'
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


a = np.mean(best, 0)
b = np.min(best, 0)
c = np.max(best, 0)
plt.plot(a)
plt.plot(b)
plt.plot(c)
plt.show()
