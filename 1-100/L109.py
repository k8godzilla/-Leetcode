#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 06:35:39 2019

@author: sunyin
"""


'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head) :
        # head : ListNode
        # return : TreeNode
        if not head:
            return head
        
        head_list = []
        while head:
            head_list.append(head)
            head = head.next
        return self.headListToBST(head_list)
            
    def headListToBST(self, headList):
        if not headList:
            return None
        
        if len(headList) == 1:
            return TreeNode(headList[0].val)
        elif len(headList) == 2:
            t0 = TreeNode(headList[0].val)
            t1 = TreeNode(headList[1].val)
            t1.left = t0
            return t1
        else:
            i_m = len(headList) // 2
            t = TreeNode(headList[i_m].val)
            t_left = self.headListToBST(headList[:i_m])
            t_right = self.headListToBST(headList[i_m + 1:])
            t.left = t_left
            t.right = t_right
            return t
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            