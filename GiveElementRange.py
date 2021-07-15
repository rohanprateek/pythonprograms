# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:11:22 2021

@author: rohan
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        
        def binsearch(nums, start, end, key):
            
            while start <= end:
                
                mid = ((end - start) // 2) + start
                
                if nums[mid] == key:
                    return mid
                
                elif nums[mid] > key:
                    end = mid - 1
                
                else:
                    start = mid + 1
            
            return None
        
        ind1 = len(A)
        ind2 = -1
        flag = 0
        
        while True:
            
            prev_ind1 = ind1 
            ind1 = binsearch(A, 0, ind1 - 1, B)
            if ind1 == None:
                break
            flag = 1
        
        while True:
            prev_ind2 = ind2
            ind2 = binsearch(A, ind2 + 1, len(A) - 1, B)
            if ind2 == None:
                break
        
        if flag:
            return [prev_ind1, prev_ind2]
        
        else:
            return [-1, -1]
            
            
        
s = Solution()
A = [5, 7, 7, 8, 8, 10]
B = 8
print(s.searchRange(A, 21))