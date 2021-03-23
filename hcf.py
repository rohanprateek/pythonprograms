# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:24:25 2021

@author: Rohan Prateek
"""

def gcd(x, y):
            if x > y:
                
                if x % y == 0:
                    return y
                
                temp = x % y
                x = y
                y = temp
                return gcd(x, y)
            
            else:
                if y % x == 0:
                    return x
                
                temp = y % x
                y = x 
                x = temp
                return gcd(x, y)
                
print(gcd(4, 10))