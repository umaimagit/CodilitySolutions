# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:34:56 2018

@author: Umaima
"""

def alternatingCharacters(s):
    
    count = 0
    
    i = 1
    comp1 = s[0]
    while i < len(s) :
        
        if s[i] == comp1:
            s.replace(s[i], "")
            print(s)
            count +=1
        else:
            comp1 = s[i]
        i += 1
            
    return count

s = "AAABBB"
res = alternatingCharacters(s)
print("Result ", res)