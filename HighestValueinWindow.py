# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:31:19 2021

@author: rohan
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):

        if B > len(A):
            return [max(A)]
        
        from collections import deque
        
        Q = deque()
        res = list()
        
        for i in range(B):
            
            while Q and A[i] >= A[Q[-1]]:
                Q.pop()
            
            Q.append(i)
        
        for i in range(B, len(A)):
            
            res.append(A[Q[0]])
            
            while Q and Q[0] <= i - B:
                Q.popleft()
                
            while Q and A[i] >= A[Q[-1]]:
                Q.pop()
                
            Q.append(i)
        
        res.append(A[Q[0]])
        
        return res

s = Solution()
A = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
B = [12, 1, 78, 90, 57, 89, 56]
print(s.slidingMaximum(A, 2))