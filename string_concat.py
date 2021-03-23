# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:11:42 2020

@author: Rohan Prateek
"""

def addStr(str1, str2):
        
        s1 = [x for x in str1]  # making list of all chars in strings
        s2 = [x for x in str2]
        
        for i in range(len(s2)): # putting all characters into single list
            s1.append(s2[i]) 
        add_list = ''.join(s1)  # joining all characters to get concatenated string
        
        return add_list
    
    
a = 'Rohan'
b = 'Prateek'
print(addStr(a, b))