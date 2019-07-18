# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:02:02 2019

@author: admin
"""

'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:      
    def postorderTraversal(self, root: TreeNode) -> list:
        # postorderTraversal(self, root: TreeNode) -> List[int]
        self.solutions = []
        self.helper(root)
        return self.solutions
        
    
    def helper(self, root):
        if root is not None:
            self.helper(root.left)
            self.helper(root.right)
            self.solutions.append(root.val)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
