# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 01:07:11 2021

@author: Rohan Prateek
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x = bin(x)[2:]
        y = bin(y)[2:]
        l = max(len(x), len(y))
        
        x = x.zfill(l)
        y = y.zfill(l)
        
        dist = 0
        
        for i in range(len(x)):
            if x[i] != y[i]:
                dist += 1
                
        return dist
    
s = Solution()
print(s.hammingDistance(2, 10))