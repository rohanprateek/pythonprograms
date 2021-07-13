# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 13:35:04 2021

@author: rohan
"""

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):

        A = [''.join(sorted(ele)) for ele in A]

        res = list()
        words = dict()

        for i in range(len(A)):
            
            if A[i] in words.keys():
                words[A[i]].append(i + 1)
            
            else:
                words[A[i]] = [i + 1]

        for k, v in words.items():
            res.append(v)
        
        return res
    
s = Solution()
A = ["cat", "dog", "god", "tca"]
print(s.anagrams(A))