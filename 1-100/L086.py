#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:08:28 2019

@author: sunyin
"""

'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        down = ListNode(0)
        up = ListNode(0)
        
        start_down = down
        start_up = up
        while head is not None:
            if head.val < x:
                down.next = head
                down = head
            else:
                up.next = head
                up = head
            head = head.next
        
        down.next = start_up.next
        if up is not None:
            up.next = None
        return start_down.next
        
        
