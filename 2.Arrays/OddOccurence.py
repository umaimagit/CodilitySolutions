# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:47:51 2018

@author: Umaima
"""

def solution(A):
    
    N = len(A)
    
#    if N == 0 or N == 1 or N == 2:
#        return A
    
    A.sort()
    #print(A)
    for i in range(0, N-1):
        
        if A[i] == A[i+1]:
            A[i] = -1
            A[i+1] = -1
        else:
            continue
        
    A.sort()
     
    return(A[N-1])
#    B = A.copy()
#    print(B)
#    for i in range(0, N-1):
#        
#        if A[i] == A[i+1]:
#            B.remove(A[i])
#            B.remove(A[i])
#    
#    return B[0]
        
    
A1 = [9,3,9,3,9,7,9]

res = solution(A1)

print("A: " + str(A1))
print("Result: " +str(res))
    
    
    
    