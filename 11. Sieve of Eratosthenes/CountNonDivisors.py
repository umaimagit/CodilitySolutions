# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:50:22 2018

@author: Umaima
"""

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    
    res = []
    
    for i in range(0, N):
        count = 0
        for j in range(0, N):
            if A[i] % A[j] != 0:
                count += 1
        res.append(count)
        
    return res

A = [3,1,2,3,6]

res = solution(A)

print("A: " + str(A))
print("Result: " + str(res))