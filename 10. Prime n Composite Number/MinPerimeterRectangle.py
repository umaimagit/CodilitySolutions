# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:58:25 2018

@author: Umaima
"""

# MinPerimeterRectangle

# Find the minimal perimeter of any rectangle whose area equals N.

def solution(N):
    # write your code in Python 3.6
    if N <=0 :
        return 0
    elif N == 1:
        return 4
    
    perimeter = []
    i = 1
    while i * i <=N:
        if N % i == 0:
           side1 = N / i
           side2 = N / side1
           perimeter.append(int(2 * (side1 + side2)))
        i += 1
           
    return min(perimeter)

A = 36

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
