# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:32:16 2019

@author: admin
"""

'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        # root : TreeNode
        # return : List[List[int]]
        
        if not root:
            return []
        res = []
        direction = 'left'
        front = [root]
        while front:
            front_next = []
            num_layer = []

            for i in range(-1, (-1) * len(front) - 1, -1):
                root_i = front[i]
                num_layer.append(root_i.val)
                if direction == 'right':
                    if root_i.right:
                        front_next.append(root_i.right)
                    if root_i.left:
                        front_next.append(root_i.left)
                else:
                    if root_i.left:
                        front_next.append(root_i.left)
                    if root_i.right:
                        front_next.append(root_i.right)
            front = front_next
            res.append(num_layer)
            if direction == 'right':
                direction = 'left'
            else:
                direction = 'right'
        return res
            
                    
        










