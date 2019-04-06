# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:19:14 2018

@author: Umaima
"""
# Test Program to find no of immediate ranks having one rank higher 
def solution(ranks):
    
    N = len(ranks)
    
    if N == 0 or N == 1:
        return 0

    count = 0
    value = -1
    ranks.sort()
    #print(ranks)
    ranks.reverse()
    #print(ranks)
    
    for i in range(1, N):
    
#        print(ranks[i])  
#        print(ranks[i-1])
        if ranks[i] == value:
            count += 1
        
        elif ranks[i] + 1 == ranks[i-1] :
                
                value = ranks[i]
                count += 1
        
    return count
        
A =  [3, 4, 3, 0, 2, 2, 3, 0, 0]

res = solution(A)

print("A: " + str(A))
print("Result: " + str(res))               
                