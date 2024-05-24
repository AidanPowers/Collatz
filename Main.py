# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:54:38 2021

@author: Aidan Powers
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

from timeit import default_timer as timer

from scipy import interpolate as intp
from scipy import integrate as intg

from numba import jit, njit, vectorize, prange ,uint64, cuda


#the number of ops required to reach 1 for a given value
@vectorize([uint64(uint64)],target='cuda') #turns this function into a high speed parallel array cruncher, if only I had a cuda gpu
def collDeg(i):
    j = 0
    while i > 1: #while it is still not true
        j = j + 1
        if i%2==0: #if even 
            i = i / 2 #divide by 2
        else: #if odd (!even) 
            i = i*3 + 1 #multiply by 3 add 1
    return(j)

def onlyUp(i):
    j = 0
    while bin(i).count("1") != 1:
        i = i*3 + 1
        j = j + 1
        #print(i)
    return j

def countTurns(i):
    binary = bin(int(i))
    t0=binary.count("0")-1
    t1=binary.count("1")
    turns = t1 - t0
    length = len(binary)-2
    return(turns)

def turnLook(i):
    j = [countTurns(i)]
    while i > 1: #while it is still not true
        #j = j + 1
        if i%2==0: #if even 
            i = i / 2 #divide by 2
        else: #if odd (!even) 
            i = i*3 + 1 #multiply by 3 add 1
        turns = countTurns(i)
        j.append(turns)
    return(j)

def floatLook(i):
    j = [countTurns(i)]
    wasEven = False
    while i > 1: #while it is still not true
        #j = j + 1
        if i%2==0 or wasEven: #if even 
            i = i / 2 #divide by 2
            wasEven = True
        else: #if odd (!even) 
            i = i*3 + 1 #multiply by 3 add 1
        j.append(i)
    return(j)


def bench(num):
    
    start = timer() #start timer

    points = np.arange(num+1, dtype=np.uint64)[1:]#creates test array
    
    dof = collDeg(points) #runs the function
    
    end = timer() #end timer
    print(end - start) #print elapsed time
    
    plt.plot(points,dof,'.')
    plt.show()
    
    #return(dof)
    
    
    
    
    
    
    
    