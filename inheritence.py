# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:57:50 2021

@author: Rohan Prateek
"""

class A:
    def __init__(self, valA, *args):
        self.a = valA
        super(A, self).__init__(*args)
        

class B(A):
    def __init__(self, valB, valA, *args):
        self.b = valB
        super(B, self).__init__(valA)

        
q = B(1, 2, 3, 4, 5)
print(q.a, q.b)
        