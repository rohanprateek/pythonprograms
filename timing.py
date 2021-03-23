# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:44:13 2021

@author: Rohan Prateek
"""

import time
start = time.time()
#start = time.clock_gettime()
for i in range(5000000):
    pass
end = time.time()
print(start, end, end - start, sep='\n')
#print(time.process_time())
