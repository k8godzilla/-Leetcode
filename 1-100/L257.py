# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:31:05 2019

@author: admin
"""

'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        # binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        path = self.helper(root)
        for i  in range(len(path)):
            path[i] = self.num2str(path[i])
        return path
        
        
        
    def num2str(self, p):
        pStr = str(p[-1])
        for i in range(len(p) - 2, -1, -1):
            pStr += '->'
            pStr += str(p[i])
        return pStr
        
        
    
    def helper(self, node : TreeNode):
        if node.left is None and node.right is None:
            return [[node.val]]
        else:
            pathLeft, pathRight = [], []
            if node.left is not None:
                pathLeft = self.helper(node.left)
            if node.right is not None:
                pathRight = self.helper(node.right)
            for i in range(len(pathLeft)):
                pathLeft[i].append(node.val)
            for i in range(len(pathRight)):
                pathRight[i].append(node.val)
            return pathLeft + pathRight
        
        

        
        

















