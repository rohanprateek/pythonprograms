# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:44:24 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        
        first = 0
        second = 0
        
        while first < len(A) and second < len(B):
            if A[first] > B[second]:
                A[first], B[second] = B[second], A[first]
                first += 1
                if B[second] > B[second + 1]:
                    ind = second + 1
                    ele = B[second]
                    while ele > B[ind]:
                        
                        B[ind - 1] = B[ind]
                        ind += 1
                        if ind == len(B):
                            break
                    B[ind - 1] = ele
            
            else:
                first += 1
        
    
        for i in range(second, len(B)):
            A.append(B[i])
            
        return A
                
            
s = Solution()
a = [-4, 3]
b = [-2, -2]
print(s.merge(a, b))