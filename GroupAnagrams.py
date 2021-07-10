# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:15:28 2021

@author: rohan
"""

class Solution:
    def groupAnagrams(self, strs: []) -> [[]]:
        
        temp = list(strs)
        strs = [''.join(sorted(ele)) for ele in strs]
        ana = dict()
        
        for i in range(len(strs)):
            
            if strs[i] in ana.keys():
                ana[strs[i]].append(temp[i])
            
            else:
                ana[strs[i]] = [temp[i]]
                
        return list(ana.values())
        
s = Solution()
A = ["eat","tea","tan","ate","nat","bat"]
B = [""]
C = ["a"]
print(s.groupAnagrams(C))  
            
        
        