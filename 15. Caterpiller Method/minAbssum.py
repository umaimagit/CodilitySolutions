# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:51:26 2018

@author: Umaima
"""
    
def solution(A):
    value = 2000000000
    front_ptr = 0
    back_ptr = len(A)-1
    A.sort()
     
    while front_ptr <= back_ptr:
        value = min(value, abs(A[front_ptr] + A[back_ptr]))
        if abs(A[front_ptr]) > abs(A[back_ptr]):
            front_ptr += 1
        else:
            back_ptr -= 1
             
    return value

A = [1,-3]

res = solution(A)

print("A: " + str(A))
print("Result: " + str(res))
    
    