# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:28:00 2018

@author: Umaima
"""

def solution(N, A):
    
    M = len(A)
    
    counter = [0] * N
    
    offset = maxcounter = 0
    
    for i in range(0, M):
        
        if A[i] > N:
            
            offset = maxcounter
            
        else:
            
            counter[A[i]-1] = max(offset + 1, counter[A[i]-1] + 1)
            
            if maxcounter < counter[A[i]-1]:
                maxcounter = counter[A[i]-1]
    
    for i in range(0, N):
        if counter[i] < offset:
            counter[i] = offset
            
    return counter

A = [3,4,4,6,1,4,4]
N = 5

res = solution(N, A)

print("A: " + str(A))
print("N ", N)
print("Result: " +str(res))