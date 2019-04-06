# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:26:11 2018

@author: Umaima
"""
#MinAvgTwoSlice

#Find the minimal average of any slice containing at least two elements.

def solution(A):
    
    if len(A) == 0:
        return 0
    
    index = 0
    minavg = 10001
    
    for i in range(0,len(A)-1):

        
        if (A[i] + A[i+1]) / 2.0 < minavg:
            minavg = (A[i] + A[i+1]) / 2.0
            index = i
        
        if i < len(A) - 2 and (A[i] + A[i+1] + A[i+2]) / 3.0 < minavg:
            minavg =  (A[i] + A[i+1] + A[i+2]) / 3.0
            index = i
            
    return index

A = [4, 2, 2, 5, 1, 5, 8]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
