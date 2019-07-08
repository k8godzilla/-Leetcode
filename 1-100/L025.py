#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 17:09:18 2019

@author: sunyin
"""


'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution:
    def reverseKGroup(self, head, k) :
        ### head : ListNode
        ### k : int
        ### return ListNode
        
        if head is None:
            return head
        
        cache = []
        count = 0
        while head is not None and count <= 2 * k:
            cache.append(head)
            head = head.next
            count += 1
            
            
        if len(cache) < k:
            return cache[0]
        
        if len(cache) == k:
            cache[0].next = None
            for j in range(k - 1, 0, -1):
                cache[j].next = cache[j - 1]
            return cache[k - 1]
        
        if len(cache) < 2 * k:
            cache[0].next = cache[k]
            for j in range(k - 1, 0, -1):
                cache[j].next = cache[j - 1]
            return cache[k - 1]
            
        else:
            res = cache[k - 1]
        
'''
        
import copy       
        
class Solution:
    def reverseKGroup(self, head, k):
        dummy_N, dummy_O = ListNode(0), ListNode(0)
        dummy_O.next = head
        length, node = 0, head
        while node:
            length += 1
            node = node.next
        node_N = dummy_N
        for _ in range(length//k):
            tail0 = dummy_O.next
            for _ in range(k):

                node_O = dummy_O.next
                
                dummy_O.next = node_O.next
                node_O.next = node_N.next

                node_N.next = node_O
                print(node_O.val)
                #try:
                    #print(node_O.val)
                #    print(dummy_N.next.val)
                #except:
                #    print('None')
                a = copy.deepcopy(dummy_N)
                a_list = []
                while a is not None:
                    a_list.append(a.val)
                    a = a.next
                print(a_list)
                
                
            node_N = tail0
        node_N.next = dummy_O.next
        return dummy_N.next        

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None         
        
tests = list(range(10))
   
lists = []
for i in range(len(tests)):
    lists.append(ListNode(tests[i]))
 
for i in range(len(tests) - 1):
    lists[i].next = lists[i + 1]
       
cl = Solution()
res = cl.reverseKGroup(lists[0], 3)
        
'''       
while res is not None:
    print(res.val)
    res = res.next      
        
'''
        
        
        
        
        
        
        