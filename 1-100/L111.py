#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 06:58:05 2019

@author: sunyin
"""

'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        # root : TreeNode
        # return : int
        
        if not root:
            return 0
        
        front = []
        if not root.left:
            front.append(root.left)
        if not root.right:
            front.append(root.right)
            
        min_depth = 1
        while front:
            min_depth += 1
            front_next = []
            leaf_found = False
            for i in range(len(front)):
                f_i = front[i]
                leaf_i = 0
                if not f_i.left:
                    front_next.append(f_i.left)
                    leaf_i += 1
                if not f_i.right:
                    front_next.append(f_i.right)
                    leaf_i += 1
                if leaf_i == 0:
                    leaf_found = True
                    break
            if leaf_found:
                break
            front = front_next
        return min_depth
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


