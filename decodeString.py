# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:57:01 2020

@author: Rohan Prateek
"""
nums = list()
res = str()
temp = str()
sub_str = list()
m = int()
count = 0
s = '100[a]'  # this string is decoded
n = 0
while n < len(s):
    
    if s[n] >= '0' and s[n] <= '9':
        if s[n + 1] >= '0' and s[n + 1] <= '9':
            if s[n + 2] >= '0' and s[n + 2] <= '9':
                num = int(s[n] + s[n + 1] + s[n + 2])
                nums.append(num)
                n = n + 3
                continue
            else:
                num = int(s[n] + s[n + 1])
                nums.append(num)
                n = n + 2
                continue
        else:
            nums.append(int(s[n]))
    
    elif s[n] == '[':
        count += 1
        sub_str.append(temp)
        temp = str()
        
    elif s[n] == ']':
        m = nums.pop()
        temp = m * temp
        t = sub_str.pop()
        temp = t + temp
    
    else:
        temp = temp + s[n]
    n += 1
res = res + temp
print(res)
    
        