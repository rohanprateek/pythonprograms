# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:49:22 2021

@author: Rohan Prateek
"""
N = 5
a = [[1], [1, 1]]

while len(a) < N:
    
    temp = a[-1]
    new = list()
    new.append(1)
    ind = 0
    while ind < len(temp) - 1:
       new.append(temp[ind] + temp[ind + 1])
       ind += 1
    new.append(1)
    a.append(new)
    
print(a)
        
    