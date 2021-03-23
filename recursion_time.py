# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:55:08 2021

@author: Rohan Prateek
"""
func_t = [2, 2] 
import time

def t(n):
    
    temp = 0
    if n == 1 or n == 0:
        return 2
    for i in range(1, n):
        temp +=  2*t(i)*t(i - 1)
        
    return temp

def t_dy(n):
    
    global func_t
    
    while len(func_t) < n:
        l = len(func_t)
        temp = func_t[l - 1] * (1 + 2 * func_t[l - 2])
        func_t.append(temp)
            
    return func_t[n - 1]
            

results = list()
dur = list()

for i in range(1, 20):
    print(i)
    start = time.time_ns()
    res = t(i)
    stop = time.time_ns()
    results.append(res)
    dur.append(stop - start)
    
print(dur)
print(t(3))
print(t_dy(4))
print(func_t)

