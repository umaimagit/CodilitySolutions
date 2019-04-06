# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:58:51 2018

@author: Umaima
"""

# test 3 correct code
def solution(S):
    
    N = len(S)
    
    if N == 0:
        return 0
    
    res = [0]
    start = ""
    end = ""
    
    ecount = N-1
    for i in range(0, N):
        
        start = start + S[i]
       
        end = S[ecount] + end
        ecount = ecount - 1
        
        if start == end:
            res.append(len(start))

    res.pop()
    
    return max(res)

S = "abbabba"
#S = "codility"
res = solution(S)

print("S ",S)
print("Res ",res)