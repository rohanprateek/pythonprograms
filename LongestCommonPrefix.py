# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:34:57 2021

@author: rohan
"""

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):

        if len(A) == 0:
            return str()

        if len(A) == 1:
            return A[0]

        A.sort()
        lcp = A[0]
        ind = 1

        while ind < len(A):
            
            temp = A[ind]
            temp_ind = 0
            s = str()

            while temp_ind < min(len(temp), len(lcp)):
                if temp[temp_ind] == lcp[temp_ind]:
                    s += temp[temp_ind]
                    temp_ind += 1
                else:
                    break
            
                
            lcp = s
            if len(lcp) == 0:
                return str()
            
            ind += 1
        
        return lcp

s = Solution()
A = [ "abcd", "abcd", "efgh" ]
print(s.longestCommonPrefix(A))