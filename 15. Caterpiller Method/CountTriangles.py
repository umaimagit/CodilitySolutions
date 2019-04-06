# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:36:01 2018

@author: Umaima
"""

#CountTriangles

#Count the number of triangles that can be built from a given set of edges.

def solution(A):
    
    N = len(A)
    
    if(N < 3):
        return 0
    
    A.sort()
    
    count = 0
# Below code 66 % result    
#    for i in range(0, len(A)-2):
#        for j in range(i+1, len(A) - 1):
#            for k in range(j+1, len(A)):
#                
#                if ((A[i] + A[j]) > A[k]) and ((A[j] + A[k]) > A[i]) and ((A[k] + A[i]) > A[j]):
#                    
#                    count = count + 1
    for i in range(0, N):
        z = i + 2
        for j in range(i+1, N):
           while z < N and (A[i] + A[j]) > A[z]:  
               z +=1 
           count += z - j - 1
           
    return count

A = [10,2,5,1,8,12]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
