# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:23:33 2018

@author: Umaima
"""

# Array Inversion Count (Countimg number of swaps) Merge Sort
maxval = 1000000000
def MergeSort(A):
    
    
    inversionc = 0
    if len(A)>1:
        mid = len(A) // 2
        leftlist = A[:mid]
        rightlist = A[mid:]
        
        
        inversionc = inversionc + MergeSort(leftlist)
        if inversionc > maxval:
            raise
        
        inversionc = inversionc + MergeSort(rightlist)
        if inversionc > maxval:
            raise
        
        i = 0
        j = 0
        k = 0
        
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] <= rightlist[j]:
                A[k] = leftlist[i]
                i = i+1
                
            else:
                A[k] = rightlist[j]
                j = j+1
                
                inversionc = inversionc + (len(leftlist) - i)
                if inversionc > maxval:
                    raise
            k = k +1
            
        while i < len(leftlist):
            A[k] = leftlist[i]
            i = i+1
            k = k+1
            
        while j < len(rightlist):
            A[k] = rightlist[j]
            j = j+1
            k = k+1
            
    return inversionc

def solution(A):
    
    try:
        
        return MergeSort(A)
    except:
        return -1



A = [-1,6,3,4,7,4]

res = solution(A)

print("A: " + str(A))
print("Result: " + str(res))