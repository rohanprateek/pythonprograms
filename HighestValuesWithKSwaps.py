# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:37:20 2021

@author: rohan
"""
A = "254"  
m = A

def func(s, k):
    s = list(s)
    global m
    
    if k == 0:
        return s
    
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            s[i], s[j] = s[j], s[i]
            temp = ''.join(s)
            m = max(temp, m)
            func(temp, k - 1)
            s[i], s[j] = s[j], s[i]

func(A, 1)
print(m)            
            
    