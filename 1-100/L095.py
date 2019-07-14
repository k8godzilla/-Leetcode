#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:39:13 2019

@author: sunyin
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def generateTrees(self, n):
        # n : int
        # return : List[TreeNode]
        # 所谓二叉树就是mit课程里的binarySearchTrees,左边小，右边大
        if n == 0:
            return []
        return self.generateSubTrees(list(range(1, n + 1)))
        
        
        
    def generateSubTrees(self, nums):
        # 递归 len(nums) <= 2时直接返回结果
        # 如果len(nums) > 2: 则遍历nums中的数字，递归得到起左右子树集合，左右子树集合交叉组合
        if len(nums) == 0:
            return [None]
        elif len(nums) == 1:
            return [TreeNode(nums[0])]
        elif len(nums) == 2:
            tree_pool = []
            nodeA0 = TreeNode(nums[0])
            nodeA1 = TreeNode(nums[1])
            nodeA0.right = nodeA1
            tree_pool.append(nodeA0)
            nodeB0 = TreeNode(nums[1])
            nodeB1 = TreeNode(nums[0])
            nodeB0.left = nodeB1
            tree_pool.append(nodeB0)
            return tree_pool
        else:
            tree_pool = []
            for i in range(len(nums)):
                
                trees_left = self.generateSubTrees(nums[:i])
                trees_right = self.generateSubTrees(nums[i + 1:])
                for t_left in trees_left:
                    for t_right in trees_right:
                        node_i = TreeNode(nums[i])
                        node_i.left = t_left
                        node_i.right = t_right
                        tree_pool.append(node_i)
            return tree_pool
                        
                
                
            
            
        

            
