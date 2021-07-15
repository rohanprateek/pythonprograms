# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:37:41 2021

@author: rohan
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 1:
            return s
    
        def isPalindrome(s):
            temp = ''.join(reversed(list(s)))
            return temp == s
        
        ind = 0
        l = 0
        string = str()
        
        while ind < len(s) - 1:
            for i in range(ind + 1, len(s)):
                temp = s[ind : i + 1]
                if isPalindrome(temp) and len(temp) > l:
                    l = len(temp)
                    string = temp
            
            ind += 1
                    
        return string
                    
s = Solution()
A = "asdsarwetdfgbfdchertwsfddsdadgrhjfthgjgtjegdsgfvjmghjkyt"
B = "asdsarsdfsdfgdstewrfgdxcgdftergxcbvedrtedfdagagagagagagagagagagagagagagagagdlh'fg;hlkerpiotegk,df';"
print(s.longestPalindrome(B))
