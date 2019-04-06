# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:51:08 2018

@author: Umaima
"""

# CountDistinctSlices

# Count the number of distinct slices (containing only unique numbers).

def solution(M, A):
    the_sum = 0
    front = back = 0
    seen = [False] * (M+1)
    while (front < len(A) and back < len(A)):
        while (front < len(A) and seen[A[front]] != True):
            the_sum += (front-back+1)
            seen[A[front]] = True
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen[A[back]] = False
                back += 1
                 
            seen[A[back]] = False
            back += 1
             
                 
    return min(the_sum, 1000000000)  

A = [3,4,5,5,2]
M = 6
res = solution(M, A)

print("M: ", M)
print("A: ", A)
print("Result: " +str(res))
                    