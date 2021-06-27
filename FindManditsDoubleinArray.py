# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:02:44 2021

@author: rohan
"""

class Solution:
    def checkIfExist(self, arr: []) -> bool:
        
        num = set()
        
        for i in range(len(arr)):
            
            if arr[i] % 2 == 0:
                if (arr[i] // 2) in num:
                    return True
            if (arr[i] * 2) in num:
                return True
            
            num.add(arr[i])
            
        return False
    
s = Solution()
print(s.checkIfExist([3, 1, 7, 11]))
    
    
        