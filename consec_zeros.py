# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:10:04 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        res = 0
        count = 0
        l = 0
        for i in range(len(A)):
            
            if A[i] == 0:
                count += 1
                
            while count > B:
                if A[l] == 0:
                    count -= 1
                l += 1
                
            res = max(res, i - l + 1)
        
        return res
            
            
s = Solution()
A = [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1]
print(s.solve(A, 2))