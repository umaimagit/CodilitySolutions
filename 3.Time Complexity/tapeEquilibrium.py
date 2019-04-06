# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:46:51 2018

@author: Umaima
"""

def solution(A):
    
    N = len(A)
    
#    if N == 0 or N == 1:
#        return 0
    
    left = A[0]
    right = 0
    for i in range(1,N):
        right = right + A[i]
    
    diff = abs(right - left)
    
    for i in range(2, N):
        left = left + A[i-1]
        right = right - A[i-1]
        diffn = abs(right - left)
        if diffn <= diff:
            diff = diffn
    
    return diff  

# Below 50% solution of tape equilibrium    
#    diff = []
#    
#    
#    for i in range(1, N):
#        diff.append(abs(sum(A[0:i]) - sum(A[i:len(A)])))
        
#    return min(diff)

A = [3,1]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
    