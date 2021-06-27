# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:05:53 2021

@author: rohan
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        
        dig = list()
        while num:
            dig.append(num % 10)
            num = num // 10
        
        res = int()
        flag = 0
        
        for i in range(len(dig) - 1, -1, -1):
            if dig[i] == 6 and not flag:
                flag = 1
                dig[i] = 9
                
            res = (res * 10) + dig[i]
            
        return res
    
s = Solution()
print(s.maximum69Number(9669))
            
                
        
    
