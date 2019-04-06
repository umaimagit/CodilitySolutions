# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:59:25 2018

@author: Umaima
"""

# Distinct Values in array

def solution(A):
    
    N = len(A)
    
    if N == 0 :
        return 0
    
    B = list(set(A))
    
    return len(B)

A = []

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))