# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 22:47:57 2021

@author: Rohan Prateek
"""

def move_zeros(A):
    
    ind = 0
    end = len(A) - 1
    
    while ind < end:
        
        if A[ind] == 0:
            temp_ind = ind
            while temp_ind < end:
                
                A[temp_ind] = A[temp_ind + 1]
                temp_ind += 1
            A[end] = 0
            end -= 1
            
        if A[ind] != 0:
            ind += 1
    
    return A

a = [0, 1, 2, 4, 0, 6, 0 ,7, 0, 0, 6, 10]
print(move_zeros(a))
            
            
        