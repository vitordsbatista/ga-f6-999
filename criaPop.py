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

bits = 25
popTam = 100
k = 10


#Geração da população inicial
def popIni(indTam, popTam):
    pop = np.random.random((popTam, indTam)) > 0.5
    return pop*1

print '==Criação da população inicial'
pop = np.stack([popIni(bits*2, popTam) for _ in range(k)]
, axis=0)

np.save('pops', pop)
print '==População inicial criada com sucesso=='
