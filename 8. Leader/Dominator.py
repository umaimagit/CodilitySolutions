# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:03:26 2018

@author: Umaima
"""


#Dominator

#Find an index of an array such that its value occurs at more than half of indices in the array.

def solution(A):
    
    # Below solution 91 %    
#    N = len(A)
#    if N == 0:
#        return -1
#    elif N == 1:
#        return 0
#    elif N == 2 and A[0] == A[1]:
#        return 0
#    elif N == 2 and A[0] != A[1]:
#        return -1
#    
#    B = A.copy()
#    B.sort()
#   
#    element = A[0]
#    count = 1
#    
#    for i in range(1, N):
#        if B[i] == element:
#            count += 1
#            if count > N // 2:
#                return A.index(element)
#            
#        else:
#            element = B[i]
#            count = 1
#            
#    return -1
     
    N = len(A)
    
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
    
    count = 0
    for i in range(0,N):
        if A[i] == candidate:
            count += 1
            
    if count > N // 2:
        return A.index(candidate)
     
    return -1

A = [2,2]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))