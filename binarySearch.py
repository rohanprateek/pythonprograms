# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:20:44 2020

@author: Anand Mohan
"""
import os
import sys
print(os.path)
def binary_search(num, ele):
    first = 0
    last = len(num) - 1
#    mid = (first + last) // 2
    while first <= last:
        mid = (first + last) // 2
        if (num[mid] < ele):
            first = mid + 1
        elif (num[mid] > ele):
                last = mid  
        else:
            return mid
    return -1
            
ar = [1, 2, 3, 4, 5]

i = binary_search(ar, 1)
print('Element found at index', i)

            
            
        
        