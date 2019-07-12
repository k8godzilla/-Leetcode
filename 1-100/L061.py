# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:44:36 2019

@author: admin
"""

'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        
        if head is None:
            return head
        
        # 预存所有node
        cache = []
        while head is not None:
            cache.append(head)
            head = head.next
        
        # 截取多余的k
        k = k % len(cache)
        
        if k == 0 or len(cache) == 1:
            return cache[0]
        else:
            # 尾首相连 处理其他node 返回-k的node
            cache[-1].next = cache[0]
            cache[-1 - k].next = None
            return cache[-k]
        