# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:43:06 2021

@author: rohan
"""

class ListNode:
    
    def __init__(self, v):
        self.val = v
        self.next = None
        
A = ListNode(5)
B = ListNode(10)
C = ListNode(15)
D = ListNode(20)
E = ListNode(25)

head = A
A.next = B
B.next = C
C.next = D
D.next = E
temp = head

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        
        cur = A 
        prev = None
        temp = None
        
        while cur != None:
            
            temp = cur.next
            cur.next = prev
            prev = cur
            if temp != None:
                cur = temp
            else:
                return cur
            

s = Solution()
h = s.reverseList(head)
while h != None:
    print(h.val)
    h = h.next
    
    
        