# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 20:47:16 2021

@author: rohan
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):

        A.sort()
        sol = list()

        for i in range(len(A) - 3):
            for j in range(i + 1, len(A) - 2):
                
                start = j + 1
                end = len(A) - 1
                val = B - A[i] - A[j]
                v = set()
                while start < end:

                    if val == A[start] + A[end]:
                        if A[start] not in v or A[end] not in v:
                            temp = [A[i], A[j], A[start], A[end]]
                            temp.sort()
                            sol.append(temp)
                            v.add(A[start])
                            v.add(A[end])
                            start += 1
                            end -= 1
                    elif val > A[start] + A[end]:
                        start += 1
                    else:
                        end -= 1
        
        return sol
                        
    
s = Solution()
A = [ 9, -8, -10, -7, 7, -8, 2, 5, -2, 8]
print(s.fourSum(A, 0))
