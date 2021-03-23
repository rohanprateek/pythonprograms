# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:03:27 2021

@author: Rohan Prateek
"""

def titleToNumber(A):
    
        A = ''.join(list(reversed(A)))
        res = 0
        
        if len(A) == 1:
            return ord(A) - 64
        
        for i in range(len(A) - 1, -1, -1):
            
            if i == 0:
                res += (ord(A[i]) - 64)
            else:
                res += ((ord(A[i]) - 64)) * (26 ** i)
        return res
    
print(titleToNumber('ABA'))
            