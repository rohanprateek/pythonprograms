# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:22:17 2021

@author: rohan
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def bin2dec(bin_str):
    
            n = len(bin_str) - 1
            num = 0
            for i in range(len(bin_str)):
                num += int(bin_str[i]) * (2 ** n)
                n -= 1
        
            return num

        def dec2bin(dec_str):
    
            temp = str()
            while dec_str:
                temp += str(dec_str % 2)
                dec_str = dec_str // 2
    
            temp = ''.join(list(reversed(temp)))
    
            return temp
    
        a = bin2dec(a)
        b = bin2dec(b)
        if a + b == 0:
            return '0'
        return dec2bin(a + b)
        
        