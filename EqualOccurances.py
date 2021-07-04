# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 13:02:32 2021

@author: rohan
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        if A[0] == B:
            ar1 = [1]
            ar2 = [0]
        elif A[0] == C:
            ar1 = [0]
            ar2 = [1]
        else:
            ar1 = [0]
            ar2 = [0]
            
        for i in range(1, len(A)):
            if A[i] == B:
                ar1.append(ar1[-1] + 1)
                ar2.append(ar2[-1])
            elif A[i] == C:
                ar1.append(ar1[-1])
                ar2.append(ar2[-1] + 1)
            else:
                ar1.append(ar1[-1])
                ar2.append(ar2[-1])
        
        diff = [abs(ar1[i] - ar2[i]) for i in range(len(A))]
        
        nums = dict()
        
        for i in range(len(diff)):
            if diff[i] in nums.keys():
                nums[diff[i]] += 1
            else:
                nums[diff[i]] = 1
        
        res = nums[0]
        
        for k, v in nums.items():
            res += ((v * (v - 1)) // 2)
        
        return res
        
s = Solution()
A = [1, 2, 2, 3, 4, 1]
B = [1, 2, 1]
print(s.solve(B, 6, 10))

            
                


        
    
 