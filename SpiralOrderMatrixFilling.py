# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:05:35 2021

@author: rohan
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, n):

        A = [[0 for _ in range(n)] for _ in range(n)]

        d = 1
        count = 1
    
        row1 = 0
        row2 = n - 1
        col1 = 0
        col2 = n - 1

        while count <= n ** 2:

            if d == 1:
                i = row1
                for j in range(col1, col2 + 1):
                    A[i][j] = count
                    count += 1
                d = 2
                row1 += 1
            
            if d == 2:
                j = col2
                for i in range(row1, row2 + 1):
                    A[i][j] = count 
                    count += 1
                d = 3
                col2 -= 1
            
            if d == 3:
                i = row2
                for j in reversed(range(col1, col2 + 1)):
                    A[i][j] = count 
                    count += 1
                d = 4
                row2 -= 1
            
            if d == 4:
                j = col1
                for i in reversed(range(row1, row2 + 1)):
                    A[i][j] = count
                    count += 1
                d = 1
                col1 += 1

        return A

s = Solution()
print(s.generateMatrix(5))
