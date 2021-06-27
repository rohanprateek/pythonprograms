# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:23:07 2021

@author: rohan
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None
        
def printlist(A):
    
    if not A:
        print("List is empty...")
        return 
    while A.next != None:
        print(A.val, " -> ", end="")
        A = A.next
        if A.next == None:
            break
    print(A.val)

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):

        def revList(A):

            head = A
            prev = None
            while head != None:
                new = head.next
                head.next = prev
                prev = head
                head = new
            return prev
        
        if B == 1:
            return A
        
        cur = A
        flag = 0

        while cur != None:
            
            start = cur
            prev = None
            count = 0
            
            while count != B:
                prev = cur
                cur = cur.next
                count += 1
            
            prev.next = None
            rev = revList(start)
        
            if flag == 0:
                head = rev
                A = head
                while head.next != None:
                    head = head.next
                flag += 1
            
            else:
                while head.next != None:
                    head = head.next   
                head.next = rev
            
        return A
    
A1 = ListNode(8)
A2 = ListNode(11)
A3 = ListNode(4)
A4 = ListNode(12)
A5 = ListNode(0)
A6 = ListNode(5)

A1.next = A2
A2.next = A3
A3.next = A4
A4.next = A5
A5.next = A6

printlist(A1)

s = Solution()
B = s.reverseList(A1, 2)
printlist(B)

            

        


