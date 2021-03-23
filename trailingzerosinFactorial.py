# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:54:41 2021

@author: Rohan Prateek
"""
def trailingZeroes(A):

        if A < 5:
            return 0
        
        two = 1
        five = 1
        t = 0
        f = 0
        
        while (A // (2**two)) > 0:
            t += A // (2 ** two)
            two += 1
            
        while (A // (5**five)) > 0:
            f += A // (5 ** five)
            five += 1
            
        return min(t, f)
    
print(trailingZeroes(9247))