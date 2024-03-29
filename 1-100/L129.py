# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:06:22 2019

@author: admin
"""

'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
示例 2:

输入: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
输出: 1026
解释:
从根到叶子节点路径 4->9->5 代表数字 495.
从根到叶子节点路径 4->9->1 代表数字 491.
从根到叶子节点路径 4->0 代表数字 40.
因此，数字总和 = 495 + 491 + 40 = 1026.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if  root is None: return 0
        if root.left is None and root.right is None:
            return root.val
        
        numRoute = self.treeIteration(root)
        

        
        res = 0
        for n in numRoute:
            res += self.listToDigits(n)

        return res
        
        
        
        
        
    def treeIteration(self, node: TreeNode) -> list:
        if node is None:
            return []
        
        if node.left is None and node.right is None:
            return [[node.val]]
        
        left = self.treeIteration(node.left)
        right = self.treeIteration(node.right)
        

        for i in range(len(left)):
            left[i].append(node.val)
        for i in range(len(right)):
            right[i].append(node.val)
            
        left.extend(right)
        return left
        
        
            
        
        
    def listToDigits(self, numList):
        
        t = 1
        num = 0
        for i in range(len(numList)):
            num += numList[i] * t
            t *= 10
        return num
        
        
        











