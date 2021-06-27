# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:15:12 2021

@author: rohan
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printlist(A):
    print('Printing list')
    while A:
        print(A.val)
        A = A.next
    print('\n')
        
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        
        if A is None:
            return B

        if B is None:
            return A

        if A.val > B.val:
            head = B
            start = head
            B = B.next

        else:
            head = A
            start = head
            A = A.head
        
        while A != None or B != None:
            
            if A and B:
                
                if A.val > B.val:
                    head.next = B
                    B = B.next
                    head = head.next

                else:
                    head.next = A
                    A = A.next
                    head = head.next
                
            elif not A:
                head.next = B
                return start
            
            else:
                head.next = A
                return start

A1 = ListNode(5)
A2 = ListNode(8)
A3 = ListNode(20)

B1 = ListNode(4)
B2 = ListNode(11)
B3 = ListNode(15)

A1.next = A2
A2.next = A3

B1.next = B2
B2.next = B3

s = Solution()
a = s.mergeTwoLists(A1, B1)

while a:
    print(a.val)
    a = a.next
    

            




