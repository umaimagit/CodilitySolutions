# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:51:19 2018

@author: Umaima
"""

#Peaks
#
#Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].

def solution(A):
    
    N = len(A)
    
    peak_idx = []
    peak_cnt = 0
    
    for i in range(1, N-1):
        
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peak_idx.append(i)
    
    peak_cnt = len(peak_idx)     
    
    if peak_cnt == 0:
        return 0
    
    elif peak_cnt == 1:
        return 1
    
    for i in range(peak_cnt,0,-1):
        
        if N % i == 0:
            
            size = N / i
            
            peak = [False] * i
            peakc = 0
            
            for peaki in peak_idx:
                
                idx = int(peaki // size)
                if peak[idx] == False:
                    peak[idx] = True
                    peakc += 1
                    
            if peakc == i:
                return peakc
    
    return 0

A = [1,2,3,4,3,4,1,2,3,4,6,2]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
                
            
        
        
