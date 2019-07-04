# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:05:34 2019

@author: admin
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cache_list = []
        while True:
            cache_list.append(head)
            head = head.next
            if head == None:
                break
        idx_del = len(cache_list) - n
        if n == 1:
            if len(cache_list) >= 2:
                cache_list[-2].next = None
                return cache_list[0]
            else:
                return None
        if idx_del == 0:
            return cache_list[0].next
        else:
            cache_list[idx_del - 1].next = cache_list[idx_del + 1]
            return cache_list[0]
        