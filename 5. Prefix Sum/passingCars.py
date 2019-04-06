# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:44:15 2018

@author: Umaima
"""

# Passing Cars

def solution(A):
    
    N = len(A)
    
    if N <=1:
        return 0
    
    zcounter = 0
    ocounter = 0
    
#    for i in range(0, N):
#        if A[i] == 0:
#            for j in range(i+1, N):
#                if A[j] == 1:
#                    counter+=1
#                    if counter > 1000000000:
#                        return -1
    
    for i in range(0, N):
         if A[i] == 0:
             zcounter+=1
         elif A[i] == 1:
             ocounter = ocounter + zcounter
             if ocounter > 1000000000:
                    return -1
    return ocounter

A = [0,1,0,1,1]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
                    