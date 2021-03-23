# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:35:55 2020

@author: Anand Mohan
"""

d = dict()
        for k,v in enumerate(nums):
            print(k, v)
            if (v in d.keys()):
                if(d[v] != k):
                    return [d[v], k]
            else:
                key = target - v
                d[key] = k