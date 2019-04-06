# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:41:18 2018

@author: Umaima
"""
# Absolute distinct integers
def solution(A):
    
    N = len(A)
    
    if N == 0:
        return 0
    
    for i in range(0, N):
        A[i] = abs(A[i])
    
    A = list(set(A))    
    return len(A)

A = [36,-36]

res = solution(A)

print("A: " + str(A))
print("Result: " + str(res))
        