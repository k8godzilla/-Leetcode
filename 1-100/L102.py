# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:02:18 2019

@author: admin
"""

'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



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
    def levelOrder(self, root):
        # root : TreeNode
        # return : List[List[int]]
        

        
        res = []
        if not root:
            return res
        
        frontier = [root]
        
        while frontier:
            front_next = []
            num_layer = []
            for i in range(len(frontier)):
                root_i = frontier[i]
                num_layer.append(root_i.val)
                if root_i.left:
                    front_next.append(root_i.left)
                if root_i.right:
                    front_next.append(root_i.right)
            res.append(num_layer)
            frontier = front_next
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        