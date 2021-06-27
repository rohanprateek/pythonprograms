# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:34:03 2021

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
    # @return an integer
    def solve(self, A, B):

        pos = 0
        head = A
        while head != None:
            head = head.next
            pos += 1

        mid = (pos // 2) + 1
    
        if B > mid:
            return -1
        
        pos = 1
        while A != None:
            if pos == mid - B:
                return A.val
        
            A = A.next
            pos += 1
            
A = ListNode(630)
B = ListNode(624)
C = ListNode(85)
D = ListNode(955)
E = ListNode(757)
F = ListNode(841)
G = ListNode(967)
H = ListNode(377)
I = ListNode(932)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H
H.next = I

s = Solution()
print(s.solve(A, 2))