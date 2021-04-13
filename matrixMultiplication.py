# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:34:29 2021

@author: Rohan Prateek
"""

def multiply(A, B):
    
    if len(A[0]) != len(B):
        print('Not possible...')
        return -1
    
    res = [[0 for x in range(len(B[0]))] for y in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                
                res[i][j] += A[i][k] * B[k][j]
                
    return res

A = [[2, 0],
     [0, 2]]
B = [[2, 3],
     [3, 2]]

print(multiply(B, A))