# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:40:01 2021

@author: Rohan Prateek
"""

def func(A):
    
    count = 0
    ind = 0
    while ind < len(A):
        if ind == len(A) - 1:
            break
        elif A[ind] == A[ind + 1]:
            m = 0
            while ind - m > -1 and ind + m + 1 < len(A):
                if A[ind - m] == A[ind + m + 1]:
                    m += 1
                    count += 1
                else:
                    break
            ind += m + 1
        else:
            ind += 1
    
    return count

print(func([1, 2, 3, 3, 2, 1, 4, 4, 5, 6, 6, 5, 7, 7, 8, 8]))