# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:47:19 2018

@author: Umaima
"""
#TieRopes
#
#Tie adjacent ropes to achieve the maximum number of ropes of length >= K.

def solution(K, A):
    
    N = len(A)
    
    if N == 0 or K == 0:
        return 0
    
    count = 0
    
    temp = 0
    
    for i in range(0, N):
        if A[i] >= K:
            count += 1
            temp = 0
        else:
            temp += A[i]
            if temp >= K:
                count += 1
                temp = 0
                
    return count
 
A = [1,2,3,4,1,1,3]
K = 4
res = solution(K, A)

print("A: " + str(A))
print("K: " + str(K))
print("Result: " +str(res))