# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:45:25 2018

@author: Umaima
"""

        
def flattenList(A):
    
    N = len(A)
    
    B = []
    
    for i in range(0, N):
        
        if type(A[i]) == list:
            
            B = B + flattenList(A[i])
        
        else:
            B.append(A[i])
            
    return B

A = [1, "a", "b", [ "c", ["d",2 ] ], "e", [ [ [ "f" ] ] ] ]   

res = flattenList(A)

print(res)
            
        
        