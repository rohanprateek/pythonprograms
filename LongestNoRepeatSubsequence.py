# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:52:35 2021

@author: rohan
"""

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):

        start = 0 
        max_len = 0
        letter = dict()
        ind = 0

        while ind < len(A):

            if A[ind] in letter.keys():
                start = max(start, letter[A[ind]] + 1)
            
            max_len = max(max_len, ind - start + 1)
            
            letter[A[ind]] = ind
            
            ind += 1
        
        return max_len

s = Solution()
A = 'bbbb'
print(s.lengthOfLongestSubstring(A))