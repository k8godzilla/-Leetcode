# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:09:47 2019

@author: admin
"""

'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        length = 0
        h = head
        while h is not None:
            h = h.next
            length += 1
        
        if length == 1:
            return True
        
        idxRevStart = length // 2
        h = head
        idx = 0
        while idx < idxRevStart:
            h = h.next
            idx += 1
            
        p, n = h, h.next
        while n is not None:
            pNext = n
            nNext = n.next
            n.next = p
            p = pNext
            n = nNext
        
        c = 0
        while c < idxRevStart:

            if head.val != p.val:
                return False
            head = head.next
            p = p.next
            c += 1
        return True
            
            
h0 = ListNode(0)
h1 = ListNode(0)
#h2 = ListNode(1)
#h3 = ListNode(0)
h0.next = h1
#h1.next = h2
#h2.next = h3

cl = Solution()
res = cl.isPalindrome(h0)       
        
        
        
        
        



















