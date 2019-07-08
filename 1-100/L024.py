#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 07:27:04 2019

@author: sunyin
"""


'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    class Solution:
        def swapPairs(self, head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head

            caches = []
            while head is not None:
                caches.append(head)
                head = head.next

            for i in range(0, len(caches), 2):
                try:
                    caches[i].next = caches[i + 3]
                except:
                    try:
                        caches[i].next = caches[i + 2]
                    except:
                        caches[i].next = None


            for i in range(1, len(caches), 2):
                caches[i].next = caches[i - 1]

            return caches[1]
        
        