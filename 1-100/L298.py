# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:38:38 2019

@author: admin
"""

'''
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。

该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。

这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。

示例 1：

输入:

   1
    \
     3
    / \
   2   4
        \
         5

输出: 3

解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3
示例 2：

输入:

   2
    \
     3
    / 
   2    
  / 
 1

输出: 2 

解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            _, res = self.helper(root)
            return res
    
    def helper(self, node:TreeNode):
        if node.left is None and node.right is None:
            return 1, 1
        elif node.right is None:
            seqLeft, maxLeft = self.helper(node.left)
            if node.left.val - node.val == 1:
                seqLeft += 1
                return seqLeft, max(seqLeft, maxLeft)
            else:
                return 1, maxLeft
        elif node.left is None:
            seqRight, maxRight = self.helper(node.right)
            if node.right.val - node.val == 1:
                seqRight += 1
                return seqRight, max(seqRight, maxRight)
            else:
                return 1, maxRight
        else:
            seqLeft, maxLeft = self.helper(node.left)
            seqRight, maxRight = self.helper(node.right)
            if node.left.val - node.val == 1:
                seqLeft += 1
            else:
                seqLeft = 1
            if node.right.val - node.val == 1:
                seqRight += 1
            else:
                seqRight = 1
            return max(seqLeft, seqRight), max(seqLeft, seqRight, maxLeft, maxRight)
                
            












