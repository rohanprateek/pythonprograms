# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:02:43 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        MAX = 1000000007
        
        def multiply(A, B):
            
            res = [[0 for x in range(len(B[0]))] for y in range(len(A))]
    
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(A[0])):
                        res[i][j] += A[i][k] * B[k][j]
            
            return res
        
        mat = [[1, 1],
               [1, 0]] 
        res = [[1, 1],
                [1, 0]]
        
        A = A - 3
        
        if A % 2 == 0:
            
            num = A // 2
            for i in range(num):
                res = multiply(res, mat)
            
            res = multiply(res, res)
            return res[0][0] % MAX
            
        else:
            num = (A - 1) // 2
            for i in range(num):
                res = multiply(res, mat)
            res = multiply(res, res)
            res = multiply(res, mat)
            return res[0][0] % MAX
        
s = Solution()
print(s.solve(10001))
