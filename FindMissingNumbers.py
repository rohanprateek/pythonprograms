# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:31:12 2021

@author: rohan
"""

class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        
        res = list()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res
            
        
s = Solution()
print(s.findDisappearedNumbers([1, 2, 3, 4, 2, 3]))