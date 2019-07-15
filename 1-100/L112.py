#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 07:27:02 2019

@author: sunyin
"""

'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, target):
        # root : TreeNode
        # sum : int
        # return bool
        
        if root is None:
            return False
            
        if root.left is None and root.right is None:
            return root.val == target
        
        if root.left is not None:
            b_left = self.hasPathSum(root.left, target - root.val)
            if b_left:
                return True
        
        b_right = self.hasPathSum(root.right, target - root.val)
        return b_right
            
            
            
            
            
            
            
            
            
            
            
        
        


