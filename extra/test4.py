# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:04:16 2018

@author: Umaima
"""

# NxM matrix Minesweeper
def minesweeper(A):
    
    res = []
    M = len(A)
    N = len(A[0])
    for i in range(0, len(A)):
        
        stra = ""
        for j in range(0, len(A[i])):
            
            if A[i][j] == 'X':
                stra = stra + 'X'
            else:
                count = 0
                if j > 0 and j < N: 
                    if A[i][j-1] == 'X':
                        count += 1
                
                if j > 0 and j <N:    
                    if A[i][j+1] == 'X':
                        count += 1
                
                if i > 0 and i < M:   
                    if A[i-1][j] == 'X':
                        count += 1
                
                if i > 0 and i < M:    
                    if A[i+1][j] == 'X':
                        count += 1
                
                if i > 0 and i < M and j > 0 and j < N:  
                    if A[i-1][j-1] == 'X':
                        count += 1
                
                if i > 0 and i < M and j > 0 and j < N:    
                    if A[i-1][j+1] == 'X':
                        count += 1
                
                if i > 0 and i < M and j > 0 and j < N:  
                    if A[i+1][j-1] == 'X':
                        count += 1
                
                if i > 0 and i < M and j > 0 and j < N:   
                    if A[i+1][j+1] == 'X':
                        count += 1
                
    
                stra = stra + str(count)
        res.append(stra)
    
    for item in res:
        print(item)
        
A =  ["OOOXXXOXX", "XXXXXXOXX", "XOOXXXXXX", "OOXXOXOXX", "XXXXXXXXX"]
print(A)
minesweeper(A)