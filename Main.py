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

from numba import jit, njit, vectorize, prange ,uint64


#the number of ops required to reach 1 for a given value
@vectorize([uint64(uint64)],target='parallel') #turns this function into a high speed parallel array cruncher, if only I had a cuda gpu
def collDeg(i):
    j = 0
    while i > 1: #while it is still not true
        j = j + 1
        if i%2==0: #if even 
            i = i / 2 #divide by 2
        else: #if odd (!even) 
            i = i*3 + 1 #multiply by 3 add 1
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
    
    
    
    
    
    
    
    