# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:43:59 2018

@author: Umaima
"""

# Count factors of given number

def solution(N):
    # write your code in Python 3.6
    if N <=0 :
        return 0
    
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            
            if N == i * i:
                count += 1
            else:
                count +=2
        i += 1
        
    return count

A = 24

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))