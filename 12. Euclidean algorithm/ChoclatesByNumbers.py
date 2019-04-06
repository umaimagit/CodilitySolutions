# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:59:07 2018

@author: Umaima
"""

# ChocolatesByNumbers

# There are N chocolates in a circle. Count the number of chocolates you will eat.

# Below solution 50 %
#def solution(N, M):
#    
#    if N == 0 :
#        return 0
#    
#    if M == 0:
#        return N
#    
#    A = []
#    
#    i = 0
#    inc = 0
#    
#    test = False
#    while test == False :
#        
#        inc = (i + M) % N
#        A.append(inc)
#        if A.count(inc) > 1:
#            test = True
#        i= i + M
#     
#    return len(A) -1
def gcd(a, b):
    
    mod = a % b
    if mod == 0:
        return b
    else:
        return gcd(b, mod)
    
def solution(N, M):
    
    lcm = N * M /gcd(N, M)
    
    res = lcm / M
    
    return int(res)
    

N = 10
M = 4
res = solution(N,M)

print("N: ", N)
print("M: ", M)
print("Result: " +str(res))