# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:29:05 2018

@author: Umaima
"""

def solution(A,B):
    
    N = len(A)
    
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    if len(A) != len(B):
        return len(A)
    
    if B.count(0) == len(B) or B.count(1) == len(B):
        return len(B)
    
    count = 0
    
    for i in range (0, len(A)-1):
        if B[i] == 1 and B[i+1] == 1:
            count = count + 1
        elif B[i] == 0 and B[i+1] == 1:
            count = count + 1
        elif B[i] == 0 and B[i+1] == 0:
            count = count + 1
        elif B[i] == 1 and B[i+1] == 0:
            
            if A[i] > A[i+1]:
                B[i+1] = B[i]
                A[i+1] = A[i]
            else:
                continue
            
    return count+1

A = [1,3,2,4,5]
B = [1,0,0,0,0] 
res = solution(A,B)

print("A: " + str(A))
print("B: " + str(B))
print("Result: " +str(res))                
        
    