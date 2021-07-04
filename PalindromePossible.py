# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:25:13 2021

@author: rohan
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        nums = dict()

        for i in range(len(A)):
            
            if A[i] in nums.keys():
                nums[A[i]] += 1
            
            else:
                nums[A[i]] = 1

        n = len(A[i])
        
        if n % 2 == 1:
            flag = 0
            for k, v in nums.items():
                if v % 2 == 1 and not flag:
                    flag += 1
                
                elif v % 2 == 1:
                    return 0
            
            return 1

        else:
            for k, v in nums.items():
                if v % 2 != 0:
                    return 0
            
            return 1
                    

        return 1

s = Solution()
a = "inttnikjmjbemrberk"
b = "vnpypznzpfxyivpppxfpp"
print(s.solve(b))