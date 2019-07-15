# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:49:35 2019

@author: admin
"""

'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def isSymmetric(self, root):
        # root : TreeNode
        # return : bool
        if not root:
            return True
        else:
            return self.isTwins(root.left, root.right)
        
    
    def isTwins(self, p, q):

        
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        elif p.val != q.val:
            return False
        elif not self.isTwins(p.left, q.right):
            return False
        else:
            return self.isTwins(p.right, q.left)
            











