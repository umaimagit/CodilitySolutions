# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:04:11 2018

@author: Umaima
"""

#CountDiv

# Compute number of integers divisible by k in range [a..b].

def solution(A, B, K):
    
    if K == 0 or B < A:
        return 0
    
#    count = 0
#    i = A
#    for i in range(A, B+1):
#        if i % K == 0:
#            count += 1
    
    diff = (B//K) - (A//K)
    
    if A % K  == 0:
        return diff + 1
    else:
        return diff
   

A = 0
B = 0
K = 2

res = solution(A, B, K)

print("A: " + str(A))
print("B",B)
print("K",K)
print("Result: " +str(res)) 
