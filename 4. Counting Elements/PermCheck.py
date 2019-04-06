# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:47:11 2018

@author: Umaima
"""

#PermCheck

#Check whether array A is a permutation. 

def solution(A):
    
    N = len(A)
    
    counter = [0] * N
    
    for element in A:
        if not 1 <= element <= N:
            return 0
        else:
            if counter[element-1] != 0:
                return 0
            else: 
                counter[element-1] = 1
    return 1
    
A = [1,2,3,5]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
        
    
        
    
    