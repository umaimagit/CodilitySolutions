
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:30:15 2018

@author: Umaima
"""

# Determine whether a given string of parentheses (multiple types) is properly nested

def solution(S):
    
    N = len(S)
    
    if N == 0:
        return 1
    elif N == 1:
        return 0
    
    temp = []
    
    for i in range(0, len(S)):
        if S[i] == '(' :
            temp.append(S[i])
        
        else:
            if len(temp) == 0:
                return 0
            
            t = temp.pop()
            if t == '(' and S[i] == ')':
                continue
            
            else:
                return 0
            
    if len(temp) == 0:
        return 1
    else:
        return 0
   
S = "())"

res = solution(S)

print("S: " + S)
print("Result: " + str(res))
        
        
    