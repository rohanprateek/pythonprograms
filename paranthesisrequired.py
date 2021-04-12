# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:07:45 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        o = 0
        c = 0
        for i in range(len(A)):
            if A[i] == ')':
                if o > 0:
                    o -= 1
                else:
                    c += 1
                
            else:
                o += 1
                
        return o + c
    
s = Solution()
a = ')('
print(s.solve(a))
     