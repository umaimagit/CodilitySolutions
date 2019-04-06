# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 17:21:50 2018

@author: Umaima
"""

# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R). 

def solution(A):
    
    N = len(A)
    
    if N <3:
        return 0
    
    A.sort()
    
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

A = [-3, 1, 2, -2, 5, 6]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))