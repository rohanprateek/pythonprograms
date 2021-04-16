# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:28:27 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        
        n = len(A)
        s = 0
        cur_sum = -10000007
        
        for i in range(n):
            s = s + A[i]
            if s > cur_sum:
                cur_sum = s
            
            if s < 0:
                s = 0
        return cur_sum
    
s = Solution()
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(a))