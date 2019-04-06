# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:08:27 2018

@author: Umaima
"""
## Below solution 50 %
#def PrimeDivisors(N):
#    
#    res= []
#    i = 2
#    if N == 2:
#        return [2]
#    while i * i <= N:
#        while N % i == 0:
#            res.append(i)
#            N = N // i
#        i += 1
#        
#    if N > i:
#        res.append(N)
#    return list(set(res))
#
##print(PrimeDivisors(5))
#    
#def solution(A, B):
#    
#    N = len(A)
#    count = 0
#    
#    for i in range(0, N):
#        
#        res1 = PrimeDivisors(A[i])
#        res2 = PrimeDivisors(B[i])
#        if res1 == res2:
#            count += 1
#            
#    return count
def gcd(a, b):
    
    mod = a % b
    if mod == 0:
        return b
    else:
        return gcd(b, mod)
    
def solution(P, Q):
    # write your code in Python 3.6
    count = 0
    for i in range(0, len(P)):
        
        a,b = P[i] , Q[i]
        g = gcd(a,b)
        
        while True:
            d = gcd(a, g)
            if d == 1:
                break
            a = a/d
            
        while True:
            d = gcd(b, g)
            if d == 1:
                break
            b = b/d
            
        if a == 1 and b == 1:
            count += 1
            
    return count

P = [15,10,3]
Q = [75,30,5]

res = solution(P,Q)

print("P: " + str(P))
print("Q: " + str(Q))

print("Result: " +str(res))
                