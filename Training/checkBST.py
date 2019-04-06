# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:01:40 2019

@author: Umaima
"""
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    
    if root.left != None and root.right != None:
        if root.data > root.left.data and root.data < root.right.data:
            checkBST(root.left)
            checkBST(root.right)
        
        else:
            return False
    
    elif root.left != None and root.right == None:
        
        if root.data > root.left.data:
            checkBST(root.left)
        else:
            return False
        
    elif root.left == None and root.right != None:
        
        if root.data < root.right.data:
             checkBST(root.right)
        else:
            return False
    
    else:
        return True
    