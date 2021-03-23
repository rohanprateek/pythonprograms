# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:38:58 2021

@author: Rohan Prateek
"""
a = 10
b = a
binary = str()
while b > 0:
    binary += str(b % 2) 
    b = b // 2
    
binary = ''.join(reversed(binary))    
print(binary, bin(a))