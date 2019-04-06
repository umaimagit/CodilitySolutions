# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:14:20 2018

@author: Umaima
"""

def makeAnagram(a, b):
    
    count = 0
    if len(a) == 0 and len(b) == 0:
        return 0
    elif len(a) == 0 and len(b) != 0:
        return len(a)
    elif len(b) == 0 and len(a) != 0:
        return len(b)
    
    for i in range(0, len(a)):
        
        if a[i] not in b:
            a.replace(a[i], "")
            count += 1
    
    for i in range(0, len(b)):
        
        if b[i] not in a:
            b.replace(b[i], "")
            count += 1
            
    return count

a = "cde"
b = "abc"

res = makeAnagram(a, b)

print("a: " , a)
print("b ", b)
print("Result: " + str(res))