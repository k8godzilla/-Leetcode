# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:36:10 2019

@author: admin
"""

'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        
        cache = []
        while head is not None:
            cache.append(head)
            head = head.next
         
        node_j = ListNode(0)
        i, j = 0, len(cache) - 1
        while i <= j:
            node_j.next = cache[i]
            cache[i].next = cache[j]
            node_j = cache[j]
            i += 1
            j -= 1
        node_j.next = None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
