# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:33:34 2018

@author: Umaima
"""

def solution(A):
    
    N = len(A)
    if N == 0:
        return 0
    elif N == 1:
        return 0
    
    
# Below 66 %  
#    for i in range(0, N):
#        
#        for j in range(i+1, N):
#            
#            diff = A[j] - A[i]
#            
#            if diff > 0:
#                res.append(diff)
#    
#    if  len(res) == 0:
#        return 0
#    else:
#        return max(res)

    B = []
    for i in range(0, N- 1):
        
        B.append(A[i+1] - A[i])
    
    max_ending = max_slice = B[0]

    
    for i in range(1, len(B)):

        # max_ending = max(0, max_ending + a)  // earlier solution
        
        max_ending = max(B[i], max_ending + B[i]) 
        max_slice = max(max_slice, max_ending)

    if max_slice > 0:
        
        return max_slice
    else:
        return 0
    
A = [23171,21011,21123,21366,21013,21367]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))