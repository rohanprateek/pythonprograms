# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:42:20 2021

@author: Rohan Prateek
"""

def solve(A, B):      
    count = 0
    if A > B:
        count += 8 - A
        count += B - 1
            
    else:
        count += 8 - B
        count += A - 1
           
    for i in range(8):
        j = A - i - 1
        k = B + i + 1
        if j <= 8 and j > 0 and k > 0 and k <= 8:
            count += 1
            print(j, k)
        j = A + i + 1
        k = B - i - 1
        if j <= 8 and j > 0 and k > 0 and k <= 8:
            count += 1
            print(j, k)
                    
    return count

print(solve(2, 4))