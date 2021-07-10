# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 22:29:52 2021

@author: rohan
"""

class Solution:
    def rob(self, nums: [int]) -> int:
        
        prev1 = 0
        prev2 = 0
        
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = temp
        
        return prev1
            
s = Solution()
a = [1, 10, 2, 3, 20, 4]
print(s.rob(a))