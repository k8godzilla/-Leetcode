# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:01:16 2019

@author: admin
"""

'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, target):
        # root : TreeNode
        # target : int
        # return : List[List[int]]
        
        _, res = self.helper(root, target)
        return res
        
    
    def helper(self, node, target):
        if node is None:
            return False, []
        if node.left is None and node.right is None:
            if node.val == target:
                return True, [[node.val]]
            else:
                return False, []
        res_sub = []
        if node.left is not None:
            b_left, num_left = self.helper(node.left, target - node.val)
            if b_left:
                for num in num_left:
                    res_sub.append([node.val] + num)
        if node.right is not None:
            b_right, num_right = self.helper(node.right, target - node.val)
            if b_right:
                for num in num_right:
                    res_sub.append([node.val] + num)
        if res_sub:
            return True, res_sub
        else:
            return False, res_sub
        
    
      












