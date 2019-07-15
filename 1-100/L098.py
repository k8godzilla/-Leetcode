# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:16:41 2019

@author: admin
"""

'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
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
    def isValidBST(self, root):
        # root : TreeNode
        # return bool
        if not root:
            return True
        
        bool_left, num_left = self.validSub(root.left)
        if not bool_left:
            return False
        for num in num_left:
            if num >= root.val:
                return False
        
        bool_right, num_right = self.validSub(root.right)
        if not bool_right:
            return False
        for num in num_right:
            if num <= root.val:
                return False
        
        return True
        
    def validSub(self, subRoot):

        # 递归 : 判断的时候递归判断左树和右树是否成立 再判断节点是否大于左树的所有节点 是否小于右树的所有节点 都成立则返回True 和该子树上的所有的值
        if subRoot is None:
            return True, []
        else:
            bool_left, num_left = self.validSub(subRoot.left)
            if not bool_left:
                return False, []
            else:
                for num in num_left:
                    if num >= subRoot.val:
                        return False, []
                    
            bool_right, num_right = self.validSub(subRoot.right)
            if not bool_right:
                return False, []
            else:
                for num in num_right:
                    if num <= subRoot.val:
                        return False, []
            
            num_left.extend(num_right)
            num_left.append(subRoot.val)
            return True, num_left
        














