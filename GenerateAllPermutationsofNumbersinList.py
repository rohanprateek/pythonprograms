# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 20:45:29 2021

@author: rohan
"""

def permutation(l):
    
    if len(l) == 0:
        return list()
    
    if len(l) == 1:
        return [l]
    perm = list()
    
    for i in range(len(l)):
        
        ele = l[i]
        
        temp = l[:i] + l[i + 1:]
        
        for num in permutation(temp):
            perm.append([ele] + num)
        
    return perm

a = permutation([1, 2, 3, 4, 5])
print((a))