# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:16:40 2018

@author: Umaima
"""
#
#NumberOfDiscIntersections
#
#Compute the number of intersections in a sequence of discs.

def solution(A):
 
# Below code 50 %
    N = len(A)
    
    upperLimit = []
    lowerLimit = []
    
    count = 0
    
    for i in range(0, N):
        
        upperLimit.append(i + A[i])
        lowerLimit.append(i - A[i])
       
    
    for i in range(0, N-1):
        
        for j in range(i+1, N):
            
            if upperLimit[i] >= lowerLimit[j] and upperLimit[j] >= lowerLimit[i]:
            
                count += 1
                
                if count > 10000000:
                    return -1
    
    return count

# Below code 100 %
def solution1(A):
    discs_count = len(A)            # The total number of discs
    range_upper = [0]*discs_count   # The upper limit position of discs
    range_lower = [0]*discs_count   # The lower limit position of discs
    # Fill the limit_upper and limit_lower
    for index in  range(0, discs_count):
        range_upper[index] = index + A[index]
        range_lower[index] = index - A[index]
    range_upper.sort()
    range_lower.sort()
    range_lower_index = 0
    intersect_count = 0
    for range_upper_index in range(0, discs_count):
        # Compute for each disc
        while range_lower_index < discs_count and range_upper[range_upper_index] >= range_lower[range_lower_index]:
            # Find all the discs that:
            #    disc_center - disc_radius <= current_center + current_radius
            range_lower_index += 1
        # We must exclude some discs such that:
        #    disc_center - disc_radius <= current_center + current_radius
        #    AND
        #    disc_center + disc_radius <(=) current_center + current_radius
        # These discs are not intersected with current disc, and below the
        #    current one completely.
        # After removing, the left discs are intersected with current disc,
        #    and above the current one.
        # Attention: the current disc is intersecting itself in this result
        #    set. But it should not be. So we need to minus one to fix it.
        intersect_count += range_lower_index - range_upper_index -1
        if intersect_count > 10000000:
            return -1
    return intersect_count

A = [1,5,2,1,4,0]

res = solution(A)

print("A: " + str(A))
print("Result: " +str(res))
