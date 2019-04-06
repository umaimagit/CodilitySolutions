# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:18:22 2018

@author: Umaima
"""

def solution(A):
    
    N = len(A)
    if N == 0:
        return 0
    elif N == 1:
        return A[0]
    
# Below answer 84 %
#    res = []
#    
#    for i in range(0, N):
#        sum1 = A[i] 
#        res.append(sum1)
#        
#        for j in range(i+1, N):
#            
#            sum1 = sum1 + A[j]
#            res.append(sum1)
#            
#    return max(res)
        
    max_ending = max_slice = A[0]

    
    for i in range(1, len(A)):

        # max_ending = max(0, max_ending + a)  // earlier solution
        
        max_ending = max(A[i], max_ending + A[i]) 
        max_slice = max(max_slice, max_ending)

    return max_slice

A = [3,2,-6,4,0]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
    