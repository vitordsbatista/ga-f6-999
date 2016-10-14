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
import functions as f
import bitstring as bts
import binstr as bs
import os.path

#Parâmentros
#(-100 a 100)
path = 'data/'
gen = 200
bits = 25
preci = 5
inter = [-100, 100]
popTam = 100
mut = 0.01
cruz = 0.8
ty = 'f6+999-sem-NL-'

#Cria uma pasta para armazenar os resultados
if not os.path.exists(path):
	os.mkdir(path)

#path = 'data/'
#Leitura do arquivo com a população iniial
pops = np.load('pops.npy')

for k in range(10):
    print '===================================================='
    print 'Ensaio: ', k + 1
    melhores = np.array(())
    media = np.array(())
    piores = np.array(())
    #Geração da população inicial
    pop = pops[k]

    for i in range(gen):
        #Converte a popução para real
        popReal = f.bin2real(pop, inter, bits, preci)
        #Avaliação
        fit = f.f6(popReal[0], popReal[1])
        #=============================================
        #Seleciona os melhores e a média
        melhores = np.append(melhores, max(fit))
        media = np.append(media, np.mean(fit))
        piores = np.append(piores, min(fit))
        #Salvando a população para a exibição
        #=============================================
        #Normalização linear das aptidões dos indivíduos
        pop, fit = f.normaLin(pop, fit)
        """
        #Transforma a fitness de array para coluna
        fit = np.reshape(fit, (len(fit), 1))
        #Concatena a população e a fitness
        pop = np.hstack((pop, fit))
        #Organiza a população
        pop = pop[pop[:,-1].argsort()]
        fit = pop[:,-1]
        pop = pop[:,:-1]
        #"""
        #Seleção e cruzamento
        pop = f.selecaoRoleta(pop, fit, cruz, popTam)

        #Mutalção
        pop = f.mutacao(pop, mut)

        #Converte a pop para inteiro
        pop = pop.astype(int)
        print 'Geração: ', i, ' Melhor: ', melhores[-1]

    #Etapa para salvar o último indivíduo
    #Converte a popução para real
    popReal = f.bin2real(pop, inter, bits, preci)

    #Avaliação
    fit = f.f6(popReal[0], popReal[1])
    #Seleciona os melhores
    melhores = np.append(melhores, max(fit))
    media = np.append(media, np.mean(fit))
    piores = np.append(piores, min(fit))
    np.save(path+ty+'best-%i' %(k), melhores)
    np.save(path+ty+'mean-%i' %(k), media)
    np.save(path+ty+'worst-%i' %(k), piores)



plt.plot(melhores, label='Melhor')
plt.plot(media, 'o', label='Média')
plt.plot(piores, '-', label='Piores')
plt.xlabel('Geracoes')
plt.ylabel('f6')
plt.show()
