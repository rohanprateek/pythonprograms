# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:36:10 2021

@author: Rohan Prateek
"""
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        
        n = int(2 * len(A) - 1) 
        res = [list() for i in range(n)]
        print(res)
        for i in range(len(A)):
            for j in range(len(A)):
                print(i + j)
                res[i + j].append(A[i][j])
                
        return res
                    
                
s = Solution()
print(s.diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))