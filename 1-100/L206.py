# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:10:21 2019

@author: admin
"""

'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        caches = []
        while head is not None:
            caches.append(head)
            head = head.next
            
        if caches == []:
            return None
            
        for i in range(-1, len(caches) * (-1), -1):
            caches[i].next = caches[i - 1]
            
        caches[0].next = None
        return caches[-1]
            
            
        

