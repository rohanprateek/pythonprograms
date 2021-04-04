# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:38:00 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        
        first = 0
        second = 0
        res = list()
        
        if len(A) <= len(B):
            
            while first < len(A):
                if A[first] == B[second]:
                    res.append(A[first])
                    first += 1
                    second += 1
                
                elif A[first] < B[second]:
                    first += 1
                    
                else:
                    second += 1
                
                if second >= len(B):
                    break
                
        else:
            
            while second < len(B):
                if A[first] == B[second]:
                    res.append(A[first])
                    first += 1
                    second += 1
                
                elif A[first] < B[second]:
                    first += 1
                    
                else:
                    second += 1
                
                if first >= len(A):
                    break
                    
        return res        
 
s = Solution()
print(s.intersect([1, 2, 3, 4, 5], [3, 4, 6, 7, 8]))           
        
        
