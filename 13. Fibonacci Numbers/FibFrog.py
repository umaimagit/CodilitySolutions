# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:06:36 2018

@author: Umaima
"""
#FibFrog
#
#Count the minimum number of jumps required for a frog to get to the other side of a river.
def solution(A):
    
    N = len(A)
    
    if N == 0:
        return -1
    
    A.append(1)
    count = 0
    frog = -1
    
    fib = [0,1]
    
    for i in range(2, N-1):
        fib.append(fib[i-2]+fib[i-1])
        
    #print(fib)    
    
    for i in range(0, N+1):
        
        if A[i] == 1:
            diff = i - frog
            #print(diff)
            if fib.count(diff) > 0:
                frog = i
                #print(frog)
                count += 1
    
    if frog == N:
        return count
    else:
        return -1
    
A = [0,0,0,1,1,0,1,0,0,0,0]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
            
                
            
        
