# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:54:19 2018

@author: Umaima
"""

def solution(A):
    
    maxLeft = 0
    bottom = 100000000
    result = 0
    
    for height in A:
        #found new peak
        if height > maxLeft:
            depth = (maxLeft - bottom) if (maxLeft - bottom) > 0 else 0
            result = max(result, depth)
            maxLeft = height
            # bottom reset
            bottom = 100000000
            continue
        
        bottom = min(bottom, height)
        depth = height - bottom
        result = max(result, depth)
        
    return result
    
#    if len(A) < 3:
#        return 0
#    
#    floodc = [0]
#    
#    stack = []
#    
#    max1 = A[0]
#    
#    for i in range(1, len(A)):
#        
#        if len(stack) == 0 and A[i] < max1:
#            stack.append(A[i])
#        
#        elif len(stack) == 0 and A[i] > max1:
#            max1 = A[i]
#        
#        elif len(stack) != 0:
#            
#            if A[i] < stack[-1]:
#                stack.append(A[i])
#            
#            elif A[i] > stack[-1]:
#                
#                temp = min(A[i], max1)
#                floodc.append(temp - min(stack))
#                max1 = A[i]
#    
#    return max(floodc)

A = [1,3,2,1,2,1,5,3,3,4,2]

res = solution(A)

print("A: " + str(A))
print("Result: " + str(res))
                