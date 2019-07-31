# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:45:51 2019

@author: admin
"""

'''
给你一个二叉搜索树和其中的某一个结点，请你找出该结点在树中顺序后继的节点。

结点 p 的后继是值比 p.val 大的结点中键值最小的结点。

 

示例 1:



输入: root = [2,1,3], p = 1
输出: 2
解析: 这里 1 的顺序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
示例 2:



输入: root = [5,3,6,2,4,null,null,1], p = 6
输出: null
解析: 因为给出的结点没有顺序后继，所以答案就返回 null 了。
 

注意:

假如给出的结点在该树中没有顺序后继的话，请返回 null
我们保证树中每个结点的值是唯一的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/inorder-successor-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def inorderSuccessor(self, root : TreeNode, p : TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right is not None:
            node = p.right
            while True:
                if node.left is None:
                    return node
                else:
                    node = node.left
            
        

        node = root
        res = None
        while node != p:
            if p.val < node.val:
                res = node
                node = node.left
            else:
                node = node.right
        
        return res        
        
        
            
        
        
        
        
        
        









