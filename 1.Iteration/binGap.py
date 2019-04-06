# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:12:32 2019

@author: Umaima
"""

def solution(N):
    
    str1 = bin(N)
    
    str1 = str1[2:]
    
    count = 0
    oneFlag = False
    carr = [0]
    
    for i in str1:
        
        if i == '1' and oneFlag == False:
            
            oneFlag = True
        
        elif i == '1' and oneFlag == True:
            
            carr.append(count)
            count = 0
        
        else:
        
            count += 1
            
    return(max(carr))

print(solution(529))