# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:25:47 2018

@author: Umaima
"""


def solution(A):

    N = len(A)
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2 and A[0] == A[1]:
        return 1
    elif N == 2 and A[0] != A[1]:
        return 0
    
    size = 0
    
    value = -1
    
    for i in range(0, N):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
                
            else:
                size += 1
                
    candidate = -1
    if size > 0:
        candidate = value
    
    count = A.count(candidate)
    
          
    if count < N // 2:
        return 0
     
    counte = 0 
    countLeft = 0
    
    for i in range(0, N):
     
        if A[i] == candidate:
            countLeft += 1
        
        #if countLeft > len(first) // 2 and count - countLeft > len(second) // 2:
        if countLeft > (i + 1) // 2 and count - countLeft > (N - i - 1) // 2:
            counte += 1
       
    return counte
    
    
A = [4,3,4,4,4,2]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
        
        
        
    