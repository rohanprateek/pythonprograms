# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:57:17 2021

@author: Rohan Prateek
"""
a = [1,1,4,2,1,3]
n = len(a)
res = list()
for i in range(n - 1):
    print(a[i], a[i + 1:])
    small = min(a[i + 1:])
    ind = a[i + 1:].index(small)
    if a[i] > small:
        res.append(a[i])
        a[ind + i + 1] = a[i]
        a[i] = small 
        res.append(small)
    
res = list(set(res))            
print('\n\n\n', a, len(res), sep='\n')


            