# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:30:06 2018

@author: Umaima
"""
# Below solution 55 %
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    res = []    
    
    # Find Semi primes 
    i = 2
    while i * i <=n:
      if prime[i] == True:
        for j in range(i*i, n+1, i):
            if j % i == 0 and prime[j//i] == True:
                res.append(j)
      i += 1
    return res

def solution(N, P, Q):
    
    M = len(P)
#    A = SieveOfEratosthenes(N)
#    semip = []
    semip = SieveOfEratosthenes(N)
    prefix = [0] * (N+1)
#    for j in range(0, len(A)):
#        
#        for k in range(j, len(A)):
#            prod = A[j] * A[k]
#            
#            if prod <= N:
#                semip.append(prod)
#            else:
#                break
    semip.sort()
    for i in range(4, N+1):
        
        if i in semip:
            prefix[i] = prefix[i-1] + 1
        else:
            prefix[i] = prefix[i-1]
        
        
    print(semip)
    print(prefix)             
    result = []
#    for i in range(0, M):
#        count = 0
#        for k in range(0, len(semip)):
#            
#            if P[i] <= semip[k] and semip[k] <= Q[i]:
#                count += 1
#        result.append(count)
    for i in range(0, M):
        
        result.append(prefix[Q[i]] - prefix[P[i]-1])
        
    return result
            
P = [1,4,16]
Q = [26,10,20]
N = 26
res = solution(N,P,Q)

print("P: " + str(P))
print("Q: " + str(Q))
print("N: " + str(N))
print("Result: " +str(res))
                
        
