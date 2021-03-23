# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:32:46 2021

@author: Rohan Prateek
"""

import matplotlib.pyplot as plt
import numpy as np

y = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
t = np.arange(len(y))
count_out, count_in = 0, 0
for i in range(len(y) - 1):
    count_out += 1
    for j in range(i + 1, len(y)):
        count_in += 1
        if y[i] > y[j]:
            y[j], y[i] = y[i], y[j]
    plt.bar(t, y)
    plt.show()
    
print('Outer loop executions = %d\nInner loop executions = %d' %(count_out, count_in))
