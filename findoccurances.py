# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:38:51 2021

@author: Rohan Prateek
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        
        def bsearch(a, ele, d):
            
            start = 0
            end = len(a) - 1
            res = -1
            while start <= end:
                mid = start + ((end - start) // 2)
                if a[mid] == ele:
                    res = mid
                    if d == 0:
                        end = mid - 1
                    else:
                        start = mid + 1
                        
                elif a[mid] > ele:
                    end = mid - 1
                    
                else:
                    start = mid + 1
                    
            return res
            
        s = bsearch(A, B, 0)
        if s == -1:
            return 0
        e = bsearch(A, B, 1)
        return e - s + 1

s = Solution()
A = [ 3, 3, 3, 3, 3, 3, 3 ]
print(s.findCount(A, 3))