# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:22:23 2018

@author: Umaima
"""

#class Tree(object):
#  x = 0
#  l = None
#  r = None


class Tree:
    def __init__(self, value, l, r):
        self.x = value
        self.l = l
        self.r = r
        
def solution(T):
    if T.l == None and T.r == None:
        # Has no subtree
        return 0
    elif T.l == None:
        # Only has right subtree
        return 1 + solution(T.r)
    elif T.r == None:
        # Only has left subtree
        return 1 + solution(T.l)
    else:
        # Have two subtrees
        return 1 + max(solution(T.l), solution(T.r))
    
