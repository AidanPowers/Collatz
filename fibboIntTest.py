# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:31:41 2022

@author: power105
"""
from timeit import default_timer as timer

a = 1
b = 1
c = 1
digs = 1000

start = timer() #start timer

for i in range(0,digs - 3,1):
    

    c = a + b
    a = b 
    b = c
    print(c)        

end = timer() #end timer
print(end - start) #print elapsed time



# ! 
# ! 
# !                             Online Fortran Compiler.
# !                 Code, Compile, Run and Debug Fortran program online.
# ! Write your code in this editor and press "Run" button to execute it.
# ! 
# ! 
# ! ------------------------------------------------------
# ! Compute the area of a triangle using Heron's formula
# ! ------------------------------------------------------

# PROGRAM  HeronFormula
#     IMPLICIT  NONE
#     INTEGER     :: a, b, c            ! three variables
#     INTEGER     :: n, digs
#     real :: start, finish
#     call cpu_time(start)
    
#     a = 1
#     b = 1
#     c = 1
#     digs = 1000
#     do n = 1, digs -3
#         c = a + b
#         a = b   
#         b = c
#         WRITE(*,*) c  
#     end do

#     call cpu_time(finish)
#     print '("Time = ",f6.3," seconds.")',finish-start

# END PROGRAM  HeronFormula
