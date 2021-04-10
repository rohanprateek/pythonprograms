# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:48:04 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        if n < 2:
            return 0
        
        if n % 2 == 0:
            mx = max(A[0], A[1])
            mn = min(A[0], A[1])
            ind = 2
        
        else:
            mx = mn = A[0]
            ind = 1
          
        while ind < n - 1:
            
            if A[ind] < A[ind + 1]:
                mn = min(mn, A[ind])
                mx = max(mx, A[ind + 1])
            else:
                mn = min(mn, A[ind + 1])
                mx = max(mx, A[ind])
            
            ind += 1
       
        return mx + mn
            
s = Solution()
A = [ -2, 1, -4, 5, 3, 1, 3, 4, 1, 7, -4, 5]
print(s.solve(A))