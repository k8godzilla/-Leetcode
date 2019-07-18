# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:40:09 2019

@author: admin
"""

'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。


 

进阶：
你是否可以不用额外空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head : ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        period = 10
        count = 0
        self.start = head
        cache = head
        head = head.next
        cycle = False
        while head is not None:
            if cache == head:
                cycle = True
                break
            
            if count == period:
                count = 0
                period *= 10
                cache = head
                
            head = head.next
            count += 1
        
        if cycle == False:
            return None
        else:
            self.period = 1
            a = cache.next
            while a != cache:
                self.period += 1
                a = a.next
                
            c_idx = 0
            c = self.start
            while c != cache:
                c_idx += 1
                c = c.next
                
            i_start, i_end = max(c_idx - self.period, 0), c_idx
            if i_start == 0:
                if self.inCycle(0):
                    return self.start
                else:
                    i_start += 1
                    
            while i_start <= i_end:
                
                i_m = (i_start + i_end) // 2
                a0 = self.inCycle(i_m - 1)
                if a0 == True:
                    i_end = i_m - 1
                else:
                    a1 = self.inCycle(i_m)
                    if a1 == False:
                        i_start = i_m + 1
                    else:
                        c = self.start
                        for i in range(i_m):
                            c = c.next
                        return c
                
                
            

        
                
    def inCycle(self, idx):
        c = self.start
        for i in range(idx):
            c = c.next
            
        c_cache = c
        for i in range(self.period):
            c = c.next
            
        return c_cache == c
            
                
        
a0 = ListNode(3)
a1 = ListNode(2)
a2 = ListNode(0)
a3 = ListNode(-4)


a0.next =a1
a1.next = a2
a2.next = a3
a3.next = a1

cl = Solution()
res = cl.detectCycle(a0)













