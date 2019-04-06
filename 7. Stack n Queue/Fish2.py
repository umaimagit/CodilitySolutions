# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:22:42 2018

@author: Umaima
"""

# N voracious fish are moving along a river. Calculate how many fish are alive.
def solution(A,B):
    
    N = len(A)
    
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    if len(A) != len(B):
        return len(A)
    
    if B.count(0) == len(B) or B.count(1) == len(B):
        return len(B)
    
    stack = []
    diefish = 0
    
    for i in range (0, len(A)):
        if B[i] == 1:
            stack.append((A[i],B[i]))
        else:
            
                while  len(stack) > 0:
                    
                    if stack[-1][0] > A[i]:
                        diefish = diefish + 1
                        
                        break
                    else:
                        diefish = diefish + 1
                        stack.pop()
                    
                    
    
    return (N-diefish)

A = [4,3,2,1,5]
B = [0,1,0,0,0] 
res = solution(A,B)

print("A: " + str(A))
print("B: " + str(B))
print("Result: " +str(res))
                
                
        