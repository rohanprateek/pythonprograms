# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:40:19 2021

@author: Rohan Prateek
"""

n = 2**8
count = 0
S = [[]]
for i in range(1, n):
    if count % 2 == 0:
        S[0].append(i)
    
    elif count % 3 == 0:
        S[0].append(i)
        
    count += 1

count = 0
temp = list()
while len(temp) != 1:
    count = 0
    n = len(S)
    temp = list()
    for i in range(len(S[n - 1])):
        if count % 4 != 0:
            temp.append(i)
        count += 1
    S.append(temp)

for i in range(len(S)):
    print(len(S[i]))