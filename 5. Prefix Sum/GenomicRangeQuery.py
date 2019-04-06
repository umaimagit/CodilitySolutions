# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:17:58 2018

@author: Umaima
"""

#GenomicRangeQuery
#
#Find the minimal nucleotide from a range of sequence DNA.
#-----------------------------------------------------------------------
 # Below 66 percent 
#def solution(S, P, Q):
    
#    result = []
#    
#    sarr = []
#    for i in range(0,len(S)):
#        if S[i] == "A":
#            sarr.append(1)
#        elif S[i] == "C":
#            sarr.append(2)
#        elif S[i] == "G":
#            sarr.append(3)
#        elif S[i] == "T":
#            sarr.append(4)
#     
#    for i in range(0, len(P)):
#        
#        temp = sarr[P[i]:Q[i]+1]
#        result.append(min(temp))
#        
#    
#    return result
 
def solution(S, P, Q):
    n = len(S)
    sumA = [0]*(n+1)
    sumC = [0]*(n+1)
    sumG = [0]*(n+1)
    sumT = [0]*(n+1)
    for idx, nucleotide in enumerate(S):
        sumA[idx+1] = sumA[idx]
        sumC[idx+1] = sumC[idx]
        sumT[idx+1] = sumT[idx]
        sumG[idx+1] = sumG[idx]
        if nucleotide == 'A':
            sumA[idx+1] += 1
        elif nucleotide == 'C':
            sumC[idx+1] += 1
        elif nucleotide == 'G':
            sumG[idx+1] += 1
        else:
            sumT[idx+1] += 1
    result = [0]*len(P)
    for i in range(len(P)):
        AsInRange = sumA[Q[i] + 1]- sumA[P[i]]
        CsInRange = sumC[Q[i] + 1]- sumC[P[i]]
        GsInRange = sumG[Q[i] + 1]- sumG[P[i]]
        #TsInRange = sumT[Q[i] + 1]- sumT[P[i]]
        if AsInRange > 0:
            result[i] = 1
        elif CsInRange > 0:
            result[i] = 2
        elif GsInRange > 0:
            result[i] = 3
        else:
            result[i] = 4
    return result

P = [2,5,0]
Q = [4,5,6]
S = "CAGCCTA"
res = solution(S, P, Q)

print("S: " + str(S))
print("P: " + str(P))
print("Q: " + str(Q))
print("Result: " +str(res))
        