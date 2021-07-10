# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 13:49:00 2021

@author: rohan
"""

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            
            temp = 0
            
            while num:
                temp += (num % 10)
                num //= 10
            
            num = temp
            
        return num
        
        
        
s = Solution()
print(s.addDigits(28))