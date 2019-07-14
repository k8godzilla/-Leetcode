#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:40:51 2019

@author: sunyin
"""

'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        
        count = 1
        start = ListNode(0)
        res = start
        
        while head is not None:
            # count < m时 顺序传导
            if count < m:
                start.next = head
                head = head.next
                start = start.next
            # keep 一个head_m代表反转的起点
            # head_p - 下一个head指向的节点
            elif count == m:
                # keep 一个head_m代表反转的起点
                # head_p - 下一个head指向的节点
                head_m = head
                head_p = head
                # 防止原地旋转 m == n
                start.next = head
                head = head.next
            elif count > m and count < n:
                head_next = head.next
                head.next = head_p
                head_p = head
                head = head_next
            elif count == n:
                start.next = head
                head_next = head.next
                head.next = head_p
                head = head_next
                head_m.next = head
            elif count > n:
                head = head.next
            count += 1
        return res.next