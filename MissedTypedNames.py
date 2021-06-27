# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 20:38:03 2021

@author: rohan
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        ind = 0
        
        if len(name) > len(typed):
            return False
        
        letters1 = list()
        letters2 = list()
        
        while ind < len(name):
            
            count = 1
            val = name[ind]
            ind += 1
            if ind == len(name):
                letters1.append([val, 1])
                break
            
            while val == name[ind]:
                count += 1
                ind += 1
                if ind == len(name):
                    break
            letters1.append([val, count])
        
        ind = 0 
        
        while ind < len(typed):
        
            count = 1
            val = typed[ind]
            ind += 1
            if ind == len(typed):
                letters2.append([val, 1])
                break
            
            while val == typed[ind]:
                count += 1
                ind += 1
                if ind == len(typed):
                    break
            letters2.append([val, count])
        print(letters1, letters2, sep="\n")    
        if len(letters1) != len(letters2):
            return False
        
        for i in range(len(letters1)):
            if letters1[i][0] != letters2[i][0]:
                return False
            if letters1[i][1] > letters2[i][1]:
                return False
            
        return True  
    
s = Solution()
a = "saeed"
b = "ssaaedd"
print(s.isLongPressedName(a, b))