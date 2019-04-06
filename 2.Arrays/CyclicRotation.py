# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:01:36 2018

@author: Umaima
"""

# Program for cyclic rotation of array by k times

def solution(A, K):
    
    N = len(A)
    
    if N == 0 :
        return []
    if N == 1 or N == K:
        return A
    
    if K > N:
        K = K % N
        #K = K - N
    if K == 0:
        return A
    
    B = [0] * N
     
    for i in range(0, N):
        
        if (i + K) < N :
            B[i+K] = A[i]
            
        #elif (i + k) == N:
            #B[(i+k) - N] = A[i]
        
        else:
            B[(i+K) - N] = A[i]
        
    return B

A = [1, 2, 3, 4]
k = 101
res = solution(A, k)

print("A: " + str(A))
print("k: "+ str(k))
print("result: "+ str(res))