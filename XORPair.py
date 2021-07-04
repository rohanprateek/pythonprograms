# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:02:11 2021

@author: rohan
"""

nums = set()
res = 0
A = [5, 4, 10, 15, 7, 6]
A = [3, 6, 8, 10, 15, 50]
B = 5
for i in range(len(A)):
    if A[i] in nums:
        if A[i] ^ B not in nums:
            nums.add(A[i] ^ B)
            res += 1
    
    else:
        nums.add(A[i] ^ B)
        
print(res)