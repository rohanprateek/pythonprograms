# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:34:39 2020

@author: Rohan Prateek
"""

num = int(input('Enter number:\n\t'))
#print(num)

temp = num
inv_num = 0

while(temp):
    unit = temp % 10
    temp = temp // 10
    inv_num = 10 * inv_num + unit
    
if inv_num == num:
    print('Palindrome')

else:
    print('Not a palindrome')
    