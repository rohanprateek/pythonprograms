# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:26:55 2021

@author: rohan
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        
        cur = head.next
        prev = head
        
        while cur != None:
            
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
                
            else:
                cur = cur.next
                prev = prev.next
                
        return head
    