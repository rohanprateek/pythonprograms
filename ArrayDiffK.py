# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:47:32 2021

@author: rohan
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        
        diff = dict()
        
        for i in range(len(A)):

            if A[i] not in diff.keys():
                diff[B + A[i]] = i
                diff[A[i] - B] = i
            
            else:
                return 1

        return 0

s = Solution()
A = [ 66, 37, 46, 56, 49, 65, 62, 21, 7, 70, 13, 71, 93, 26, 18, 84, 96, 65, 92, 69, 97, 47, 6, 18, 17, 47, 28, 71, 70, 24, 46, 58, 71, 21, 30, 44, 78, 31, 45, 65, 16, 3, 22, 54, 51, 68, 19, 86, 44, 99, 53, 24, 40, 92, 38, 81, 4, 96, 1, 13, 45, 76, 77, 8, 88, 50, 89, 38, 60, 61, 49, 25, 10, 80, 49, 63, 95, 74, 29, 27, 52, 27, 40, 66, 38, 22, 85, 22, 91, 98, 19, 20, 78, 77, 48, 63, 27]
print(s.diffPossible(A, 31))