# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:42:31 2018

@author: Umaima
"""

def solution(A):
    
    N = len(A)
    if N == 0  :
        return 1
    if N == 1 and A[0] > 1:
        return A[0]-1
    
    B = A
    A.sort()
    
    for i in range(0,N-1):
        
        if A[i+1] - A[i] > 1:
            return A[i] + 1
    
    if A[0] == 2: 
        return 1
    else:
        return B[N-1] + 1



A = [3,4]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
    