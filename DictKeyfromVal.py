# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:27:36 2021

@author: Rohan Prateek
"""

a = {'a' : 10,
     'b' : 20,
     'c' : 30,
     'd' : 40,
     'e' : 50}

ele = 40

for k, v in a.items():
    if v == ele:
        print(k)