# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:40:42 2019

@author: admin
"""

'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        # root: TreeNode
        # return : List[List[int]]
        if not root:
            return []
        
        res = []
        front = [root]
        while front:
            front_next = []
            num_layer = []
            for i in range(len(front)):
                node_i = front[i]
                num_layer.append(node_i.val)
                if node_i.left:
                    front_next.append(node_i.left)
                if node_i.right:
                    front_next.append(node_i.right)
            front = front_next
            res.append(num_layer)
        res.reverse()
        return res
                
                
                
                
                
            
            
            
            
            
            
            
            
            
        
        
        


