# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:17:43 2019

@author: admin
"""

'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.heaps = []
        for node in lists:
            if node is not None:
                self.heaps.append(node)
                self.maxHeapify(-1)
        
        if self.heaps == []:
            return None
        self.res = []
        while True:
            n = self.heaps.pop()
            nn = n.next
            self.res.append(n)
            if nn is not None:
                self.heaps.append(nn)
                self.maxHeapify(-1)
            else:
                if len(self.heaps) == 0:
                    break
                else:
                    self.heaps.append(self.heaps[0])
                    self.heaps = self.heaps[1:]
                    self.maxHeapify(-1)
        for i in range(len(self.res) - 1):
            self.res[i].next = self.res[i + 1]
        self.res[-1].next = None
        return self.res[0]
                
               
    def maxHeapify(self, idx):
        if abs(idx * 2) == len(self.heaps):
            if self.heaps[2 * idx].val < self.heaps[idx].val:
                cache = self.heaps[idx]
                self.heaps[idx] = self.heaps[2 * idx]
                self.heaps[2 * idx] = cache
        elif abs(2 * idx) <  len(self.heaps):
            left = self.heaps[2 * idx]
            right = self.heaps[2 * idx - 1]
            if left.val < right.val:
                if left.val < self.heaps[idx].val:
                    cache = self.heaps[idx]
                    self.heaps[idx] = self.heaps[2 * idx]
                    self.heaps[2 * idx] = cache
                    self.maxHeapify(2 * idx)
            else:
                if right.val < self.heaps[idx].val:
                    cache = self.heaps[idx]
                    self.heaps[idx] = self.heaps[2 * idx - 1]
                    self.heaps[2 * idx - 1] = cache
                    self.maxHeapify(2 * idx - 1)
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
                
                
                
                
                
                
                
                
                
                
                
                
                
        