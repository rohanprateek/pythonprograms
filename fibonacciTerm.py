# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:18:38 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        nums = [1, 1]
        def get(k):
            if k > len(nums):
                temp = get(k - 1) + get(k - 2)
                nums.append(temp)
                return temp
            else:
                return nums[k - 1]
        
        return get(A)
    
s = Solution()
print(s.solve(25))
            
