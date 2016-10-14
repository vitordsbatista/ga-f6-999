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
import binstr as bs
from math import sin, sqrt


#Decodificação binária
def decodifica(a, _min, _max, _bits, _preci):
    resp = (float(a) * (_max - _min)/pow(2, _bits)) + _min
    return resp
    #return round(resp, _preci)

def bin2real(pop, inter, nbits, ndeci):
    x = np.array((), dtype=int)
    y = np.array((), dtype=int)
    for i in pop:
        x = np.append(x, int(''.join(str(j) for j in i[:nbits]), 2))
        y = np.append(y, int(''.join(str(j) for j in i[nbits:]), 2))

    x = [round(decodifica(i, inter[0], inter[1], nbits, ndeci), ndeci) for i in x]
    y = [round(decodifica(i, inter[0], inter[1], nbits, ndeci), ndeci) for i in y]
    return np.vstack((x, y))

#Avaliação
def f6(x, y):
    #x = [decodifica(i, _min, _max, _bits, _preci) for i in pop[:,:22]]
    #y = [decodifica(i, _min, _max, _bits, _preci) for i in pop[:,22:]]
    num = np.sin(np.sqrt(x*x + y*y))
    den = 1+0.001*(x*x + y*y)
    return 999.5 + (num*num-0.5)/(den*den)

#Normalização Linear
def normaLin(pop, fit):
    #Criação da nova aptidão
    newFit = np.array(())
    #Transforma a fitness de array para coluna
    fit = np.reshape(fit, (len(fit), 1))
    #Concatena a população e a fitness
    pop = np.hstack((pop, fit))
    #Organiza a população
    pop = pop[pop[:,-1].argsort()]
    fit = pop[:,-1]
    pop = pop[:,:-1]
    #Calcula os valores de mínimo, máximo e o tamanho da populaçãp
    #mi = min(fit)
    #ma = max(fit)
    tam = len(fit)
    mi = 1.
    ma = 50.
    for i, idn in enumerate(fit):
        #Calcula o novo valor da fitness
        f = mi + ((ma-mi)/(tam-1)) * (i-1)
        newFit = np.append(newFit, f) 
    return pop, newFit


#Geração da população inicial
def popIni(indTam, popTam):
    pop = np.random.random((popTam, indTam)) > 0.5
    return pop*1
	
def selecaoRoleta(pop, fit, cruz, popTam):
    newPop = np.zeros((1, pop.shape[1]))[:-1]
    #Etapas da criação da roleta
    somaFit = sum(fit)
    novaFit = fit/somaFit
    novaFit = np.reshape(novaFit, (100, 1))
    #Enquanto a nova população não estiver cheia
    while newPop.shape[0] != popTam:
        #Seleciona dois indivíduos
        ind1 = roleta(pop, novaFit)
        ind2 = roleta(pop, novaFit)
        #Se o cruzamento for satisfeito, então ocorre-o
        r = np.random.rand()
        if r < cruz:
            filho1, filho2 = cruzamentoUmPonto(ind1, ind2)
            newPop = np.vstack((newPop, filho1))
            newPop = np.vstack((newPop, filho2))
        else:
            newPop = np.vstack((newPop, ind1))
            newPop = np.vstack((newPop, ind2))

    return newPop

        

def roleta(pop, fit):
    r = np.random.rand()
    c = 0
    for i, ind in enumerate(pop):
        c = fit[i] + c
        if c > r:
            return ind


def cruzamentoUmPonto (ind1, ind2):
    corte = np.random.randint(1, len(ind1))
    tmp1 = ind1[:corte]
    tmp2 = ind2[:corte]
    ind1[:corte] = tmp2
    ind2[:corte] = tmp1
    return ind1, ind2

#Seleção dos pais por Torneio
def selecaoTorneio(pop, tor = 1):    
    r = pop.shape[0]
    popOut = np.array((), dtype=str)
    for i in range(r):
        #Torneio
        #Seleciona dois indivíduos aleatórios
        [a, b] = np.random.choice(r, 2, replace=False)
        ind1 = pop[a]
        ind2 = pop[b]
        #Realiza o torneio e coloca o selecionado na pop
        popOut = np.append(popOut, torneio(ind1, ind2, tor)[0])
    return popOut

#Torneio para a seleção
def torneio(ind1, ind2, tor):
    #Torneio
    rand = np.random.rand()
    #Minimizar
    if ind1[-1] > ind2[-1]:
        if tor > rand:
            return ind1
        else:
            return ind2
    else:
        if tor > rand:
            return ind2
        else:
            return ind1

#Mutação
def mutacao(pop, mut):
    for i, ind in enumerate(pop):
        for j, gen in enumerate(ind):
            r = np.random.rand()
            if mut > r:
                pop[i, j] = 1-gen
    return pop

#Cruzamento
def cruzamento(pop, cross):
    popTemp = pop.copy()
    popOut = pop.copy()
    popTemp = popTemp[:, :-1]
    for i in range(0, pop.shape[0], 2):
        if len(popTemp) < 2:
            break
        i1 = popTemp[0]
        i2 = popTemp[0]
        popTemp = popTemp[2:, :]
        rand = np.random.rand()
        if cross > rand:
            i1, i2 = crossBin(i1, i2)
        popOut[i, :-1] = i1
        popOut[i+1, :-1] = i2
    return popOut

#Cruzamento com dois pontos
def crossTwoPoints(p1, p2):
    tmp1 = p1[3:6]
    tmp2 = p2[3:6]
    p1[3:6] = tmp2
    p2[3:6] = tmp1
    return p1, p2

#Crossover uniforme
def crossBin(p1, p2):
    f1 = f2 = p2
    mask = np.random.random(indTam-1) > 0.5
    for i, gen in enumerate(mask):
        if gen is True:
            f1[i] = p1[i]
        else:
            f2[i] = p1[i]
    return f1, f2

