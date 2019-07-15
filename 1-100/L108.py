# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:49:21 2019

@author: admin
"""

'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
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
    def sortedArrayToBST(self, nums):
        # nums : List[int]
        # return : TreeNode
        
        if len(nums) == 0:
            return None
        elif  len(nums) == 1:
            return TreeNode(nums[0])
        else:
            i_m = len(nums) // 2
            node = TreeNode(nums[len(nums) // 2])
            left = self.sortedArrayToBST(nums[:i_m])
            right = self.sortedArrayToBST(nums[i_m + 1:])
            node.left = left
            node.right = right
            return node
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        


