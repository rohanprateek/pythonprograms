# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:42:01 2021

@author: Rohan Prateek
"""

def multiply(A, B):
            
    num1 = 0
    num2 = 0
	    
    while A:
        dig = int(A[0])
        num1 = 10 * num1 + dig
        A = A[1:]
	        
    while B:
        dig = int(B[0])
        num2 = 10 * num2 + dig
        B = B[1:]
            
    res = num1 * num2
    return str(res)

print(multiply("100", "3423"))

        
        