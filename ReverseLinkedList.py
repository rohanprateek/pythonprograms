# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:08:18 2021

@author: rohan
"""

class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None
        
def printlist(A):
    
    while True:
        print(A.val, " -> ", end="")
        A = A.next
        if A.next == None:
            break
    print(A.val)
    
def reverselist(A):
    
    head = A
    prev = None
    
    while head != None:
        new = head.next
        head.next = prev
        prev = head
        head = new
    return prev

A1 = ListNode(5)
A2 = ListNode(10)
A3 = ListNode(15)
A1.next = A2
A2.next = A3 

printlist(A1)

B = reverselist(A1)
printlist(B)

   
        

