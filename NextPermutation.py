# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 13:53:51 2021

@author: rohan
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, a):
        
        flag = 0
        
        for i in reversed(range(len(a) - 1)):
            if a[i] < a[i + 1]:
                flag = 1
                ind = i
                break  
        if not flag:  
            a.sort()
            return a
        
        j = next(j for j in reversed(range(ind + 1, len(a))) if a[ind] < a[j])

        a[ind], a[j] = a[j], a[ind]

        a[ind + 1:] = reversed(a[ind + 1:])
        return a


s = Solution()
A = [1, 2, 3]
B = [20, 50, 113]
C = [1, 1, 2]
D = [3, 2, 1]
E = [1, 2, 3, 6, 5, 4]
F = [1, 2, 3, 5, 4, 6]
print(s.nextPermutation(A))
print(s.nextPermutation(B))
print(s.nextPermutation(C))
print(s.nextPermutation(D))
print(s.nextPermutation(E))
print(s.nextPermutation(F))