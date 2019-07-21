# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:31:39 2019

@author: admin
"""

'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        f = dummy
        while head is not None:
            if head.val != val:
                f.next = head
                f = f.next
            head = head.next
        f.next = None
        return dummy.next
            












