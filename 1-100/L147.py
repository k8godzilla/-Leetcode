# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:07:05 2019

@author: admin
"""

'''
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        self.turbo = 10
        if head is None:
            return head
        start = ListNode(pow(2, 31) * (-1))
        start.next = head
        
        headNext = head.next
        head.next = None
        head = headNext
        while head is not None:
            startCache = start
            headNext = head.next
            self.helper(startCache, head)
            head = headNext
        return start.next

    
    def helper(self, head, node):
        while head is not None:
            count = 0
            headNext = head
            while count <= self.turbo and headNext is not None:
                headNext = headNext.next
                count += 1
            if headNext is None or headNext.val >= node.val:
                if head.val <= node.val and (head.next is None or head.next.val >= node.val):
                    cache = head.next
                    head.next = node
                    node.next = cache
                    break
            
                head = head.next
            else:
                head = headNext
        
a0 = ListNode(2)   
a1 = ListNode(4)  
a2 = ListNode(1)  
a3 = ListNode(3)

a0.next = a1
a1.next = a2
a2.next = a3

cl = Solution()    
res = cl.insertionSortList(a0)  

for i in range(8):
    print(res.val)
    res = res.next
        
       


