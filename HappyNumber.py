# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:16:23 2021

@author: rohan
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        seq = set()
        
        def sqSum(x):
            return sum([a ** 2 for a in x])
    
        def dig_sum(x):
            
            if x == 1:
                return False
            
            digits = list()
            
            while x:
                digits.append(x % 10)
                x = x // 10
                
            if sqSum(digits) == 1:
                return True
            
            if sqSum(digits) in seq:
                return False
            
            else:
                seq.add(sqSum(digits))
                if dig_sum(sqSum(digits)):
                    return True
                else:
                    return False
            
        return dig_sum(n)

s = Solution()
print(s.isHappy(2))            