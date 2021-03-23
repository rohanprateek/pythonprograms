# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:32:46 2021

@author: Rohan Prateek
"""

import matplotlib.pyplot as plt
import numpy as np

y = [5, 1, 4, 2, 8]
t = np.arange(len(y))
count_out, count_in = 0, 0  
plt.bar(t, y)
plt.show()
swap = False
for i in range(len(y)):
    count_out += 1
    for j in range(len(y) - i - 1):
        count_in += 1
        if y[j] > y[j  + 1]:
            y[j], y[j + 1] = y[j + 1], y[j]
            swap = True
    if swap == False:
        break
    plt.bar(t, y)
    plt.show()
    
print('Outer loop executions = %d\nInner loop executions = %d' %(count_out, count_in))
