# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:04:13 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        vow = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        n = len(A) - 1
        for i in range(len(A)):
            
            if A[i] in vow:
                count += n - i + 1
                
        return count

s = Solution()
string = 'sdfkdfzxmczklxLKSNVLKVSDKjlaknlknkljNKJLNKJLJHJKGJHGjhbjggfhgFGJHKHHJGFGFFGXfgfAGHFJU'
print(s.solve(string))