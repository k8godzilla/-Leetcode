#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:29:57 2019

@author: sunyin
"""

'''
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

示例：

输入: root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-univalue-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        b, v = self.helper(root)
        return self.res
    
    def helper(self, node: TreeNode):
        if node.left is None and node.right is None:
            self.res += 1
            return True, node.val
        elif node.left is None:
            b, v = self.helper(node.right)
            if b and v == node.val:
                self.res += 1
                return b, v
            else:
                return False, -1
        elif node.right is None:
            b, v = self.helper(node.left)
            if b and v == node.val:
                self.res += 1
                return b, v
            else:
                return False, -1
        else:
            bRight, vRight = self.helper(node.right)
            bLeft, vLeft = self.helper(node.left)
            
            if bRight and bLeft and vRight == node.val and vLeft == node.val:
                self.res += 1
                return True, node.val
            else:
                return False, -1
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        