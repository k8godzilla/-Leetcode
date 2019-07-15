#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 06:48:26 2019

@author: sunyin
"""

'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        # root : TreeNode
        # return : bool
        b_root, _ = self.balanceAndDepth(root)
        return b_root
        
    def balanceAndDepth(self, node):
        if not node:
            return True, 0
        
        b_left, d_left = self.balanceAndDepth(node.left)
        if not b_left:
            return False, -1
        b_right, d_right = self.balanceAndDepth(node.right)
        if not b_right:
            return False, -1
        
        if abs(d_left - d_right) > 1:
            return False, -1
        else:
            return True, max(d_left, d_right) + 1
        
        
        














