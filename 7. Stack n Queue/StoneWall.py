# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:52:51 2018

@author: Umaima
"""

#StoneWall
#
#Cover "Manhattan skyline" using the minimum number of rectangles.
def solution(H):
    
    N = len(H)
    
    stack = []
    
    count = 0
    
    for i in range(0, N):
        
        while(len(stack) != 0 and stack[-1] > H[i]):
            stack.pop()
        
        if len(stack) != 0 and stack[-1] < H[i]:
            stack.append(H[i])
            count += 1

        elif len(stack) == 0:
            stack.append(H[i])
            count += 1
            
    return count

A = [8,8,5,7,9,8,7,4,8]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
                
                