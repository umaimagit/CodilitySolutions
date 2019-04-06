# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:27:22 2018

@author: Umaima
"""

def solution(X, Y, D):
    
    if X == 0 or Y == 0 or X == Y or D == 0:
        return 0

    i = Y - X
    res = i // D
    
    if i % D == 0:
        return res
    else:
        return res + 1
    
X = 10
Y = 85
D = 30

res = solution(X, Y, D)
print("Res ", res)
    
    