# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:32:40 2021

@author: Rohan Prateek
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = list()
        ind = 0
        while ind < len(intervals):
            
            first = intervals[ind][0]
            last = intervals[ind][1]

            if ind != len(intervals) - 1:
                while last >= intervals[ind + 1][0]:
                
                    if intervals[ind + 1][1] > last:
                        last = intervals[ind + 1][1]
                    ind += 1
                    if ind == len(intervals) - 1:
                        break
                
            res.append([first, last])
            ind += 1
            
        return res
                
                
                
                
                
        