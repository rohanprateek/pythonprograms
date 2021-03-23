# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:54:38 2021

@author: Rohan Prateek
"""

def isPalindrome(A):
    
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] != A[j]:
            return False
        i += 1
        j -= 1  
    return True

A = 'rvaravr'
print(isPalindrome(A))
count = 0 
while len(A) > 0:
    if isPalindrome(A):
        break
    else:
        A = A[ : -1]
        count += 1

print(count)
        