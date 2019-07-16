# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:29:52 2019

@author: admin
"""

'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        # root : TreeNode
        # return : None
        """
        Do not return anything, modify root in-place instead.
        """
        if not root : return root
        
        #starter = root
        
        end = self.helper(root)
        
        
        
    def helper(self, node):
        if not node : return node
        
        left = node.left
        right = node.right
        
        if not left:
            node.right = left
            node.left = None
            node = self.helper(left)
        if not right:
            node.right = right
            node.left = None
            node = self.helper(right)
        return node















