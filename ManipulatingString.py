# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 17:31:46 2021

@author: rohan
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        res = list(A)
        occur = dict()

        for i in range(len(A)):
            if A[i] not in occur.keys():
                occur[A[i]] = i

            else:
                res[occur[A[i]]] += 1

        return res  

s = Solution()
A = [ 1, 2, 3, 2, 3, 1, 4, 2, 1, 3 ]
print(s.solve(A))