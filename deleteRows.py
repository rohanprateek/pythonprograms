# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:18:31 2021

@author: rohan
"""

class Solution:
    def minDeletionSize(self, strs):
        
        a = [[x[i] for x in strs] for i in range(len(strs[0]))]
        
        ans = 0
        
        for let in a:
            if sorted(let) != let:
                ans += 1
                
        return ans

s = Solution()
print(s.minDeletionSize(["cba","daf","ghi"]))