 # -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:11:02 2021

@author: Rohan Prateek
"""

from random import sample

def gen_list(k):
    
    s = list(S)
    temp = s[0]
    seed = 1
    while seed > 0:
        seed0 = seed
        seed = int(round((len(temp) * k) + 0.001))
        if seed == 0 or seed0 == seed:
            break
        temp = sample(temp, k=seed)
        temp.sort()
        s.append(temp)
    
    return s
        


def search(S, key):
    
    n = len(S) - 1
    
    if key == S[n][0]:
        return S[0].index(key), 1
        
    elif key > S[n][0]:
        ele = S[n][0]
        comp = 1
        direction = 'f'
        n -= 1
    
    else:
        ele = S[n][0]
        comp = 1
        direction = 'b'
        n -= 1
    
    while n >= 0:
        temp = S[n]
        ind = temp.index(ele)
        print(ind, temp[ind])
        ele = None
        
        if direction == 'f':
            ele = temp[-1]
            for i in range(ind + 1, len(temp)):
                comp += 1
                if key < temp[i]:
                    ele = temp[i - 1]
                    n -= 1
                    break
        
        else:
            ele = temp[0]
            for i in range(ind + 1, -1, -1):
                comp += 1
                if key > temp[i]:
                    ele = temp[i]
                    n -= 1
                    direction = 'f'
                    break
   
    return ind, comp    
                       
    
n = 2**8
count = 0
S = [[]]

for i in range(1, n):
    if count % 2 == 0:
        S[0].append(i)
    
    elif count % 3 == 0:
        S[0].append(i)
        
    count += 1
    
S_half = gen_list(0.5)            
S_quarter = gen_list(0.25)
S_tf = gen_list(0.75)
search(S_tf, 255)


