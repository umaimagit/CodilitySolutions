# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:08:58 2018

@author: Umaima
"""

# Determine whether a triangle can be built from a given set of edges. 

def solution(A):
    
    N = len(A)
    
    if(N < 3):
        return 0
    
    A.sort()
    
#    for i in range(0, len(A)-2):
#        for j in range(i+1, len(A) - 1):
#            for k in range(j+1, len(A)):
#                
#                if A[i] + A[j] > A[k] and A[j] + A[k] > A[i] and A[k] + A[i] > A[j]:
#                    
#                    return 1
    for i in range(0, len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
        
    return 0

A = [10,2,5,1,8,21]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
    