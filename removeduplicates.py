# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:31:52 2021

@author: Rohan Prateek
"""

def remove(A):
    
    ind = 1
    end = len(A) - 1
    
    while ind <= end:

        if A[ind] == A[ind - 1]:
            temp_ind = ind - 1
            count = 0
            while A[ind] == A[temp_ind]:
                ind += 1
                count += 1
                if ind == len(A):
                    return A[:temp_ind + 1], temp_ind + 1
                    break
            temp_ind2 = ind
            A[temp_ind + 1:] = A[temp_ind2:]
            end -= count
            ind = temp_ind + 1
        
        else:
            ind += 1
    
    return A[:end + 1], end + 1

arr = [ 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3 ]
print(remove(arr))            
         
        
        
        