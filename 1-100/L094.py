#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:09:52 2019

@author: sunyin
"""

'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # root 可能为None
        # 关键搞明白什么叫中序遍历
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            self.res.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
        return self.res
       
            
