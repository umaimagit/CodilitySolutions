# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:12:18 2018

@author: Umaima
"""

def solution(P, C):
    
    for i in range(C,0,-1):
        
        if P >= 2 * C:
            return C
        
    return 0