# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:03:03 2018

@author: Umaima
"""
#Find the earliest time when a frog can jump to the other side of a river. 
def solution(X, A):
    
    N = len(A)
    if N == 0 or X == 0 or N < X or X < 0:
        return -1
 #solution below with less than 100 %    
    X1 = [False] * X 
    tocover = X
    for i in range(0, N):
        
        if A[i] <= len(X1):
            if X1[A[i]-1] == False:
                X1[A[i]-1] = True
                tocover -= 1
            
#            if X1.count(0) > 0 :
#                continue
#            else:
#                return i
            if tocover == 0:
                 return i
    return -1
        
   
       
A = [3,1,11,2,3]
X = 1
res = solution(X, A)

print("A: " + str(A))
print("Result: " +str(res))
    
        
        