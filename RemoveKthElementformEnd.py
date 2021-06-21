# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:48:57 2021

@author: rohan
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):

        l = 0
        head = A
        while head != None:
            l += 1
            head = head.next
        
        if B > l and l > 1:
            A = A.next
            return A
        
        if B > l:
            return None
        
        if l == 1:
            return None

        n = l - B + 1

        if n == 1:
            A = A.next
            return A

        pos = 1
        head = A

        while pos != n - 1:
            print(pos)
            head = head.next
            pos += 1

        head.next = head.next.next

        return A

A = ListNode(5)
B = ListNode(10)
C = ListNode(15)
D = ListNode(20)
A.next = B
B.next = C
C.next = D

s = Solution()
a = s.removeNthFromEnd(A, 2)
while a != None:
    print(a.val)
    a = a.next
    

        



