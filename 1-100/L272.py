# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 17:49:40 2019

@author: admin
"""

'''
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。

注意：

给定的目标值 target 是一个浮点数
你可以默认 k 值永远是有效的，即 k ≤ 总结点数
题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值
示例：

输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2

    4
   / \
  2   5
 / \
1   3

输出: [4,3]
拓展：
假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（n 为总结点数）的时间复杂度内解决该问题呢？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> list:
    # def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        if k == 0:
            return []
        
        if root == None:
            return []
        
        
        # find closest node
        diff = pow(2, 31)
        node = root
        nodeC = None
        while node != None:
            if abs(node.val - target) < diff:
                nodeC = node
                diff = abs(node.val - target)
            if node.val < target:
                node = node.right
            elif node.val > target:
                node = node.left
            else:
                node = None
                
        res = [nodeC.val]
        nodeRight = self.nextGreater(nodeC, root)
        nodeLeft = self.nextSmaller(nodeC, root)
        while len(res) < k:
            if nodeRight is None:
                res.append(nodeLeft.val)
                nodeLeft = self.nextSmaller(nodeLeft, root)
            elif nodeLeft is None:
                res.append(nodeRight.val)
                nodeRight = self.nextGreater(nodeRight, root)
            elif abs(nodeLeft.val - target) < abs(nodeRight.val - target):
                res.append(nodeLeft.val)
                nodeLeft = self.nextSmaller(nodeLeft, root)
            else:
                res.append(nodeRight.val)
                nodeRight = self.nextGreater(nodeRight, root)
                
        return res

       
    def nextGreater(self, p: TreeNode, root: TreeNode):
        if p is None:
            return None
        
        if p.right is not None:
            p = p.right
            while p.left is not None:
                p = p.left
            return p
        

        node = root
        res = None
        while node != p:
            if p.val < node.val:
                res = node
                node = node.left
            else:
                node = node.right
        
        return res  

    def nextSmaller(self, p: TreeNode, root: TreeNode):
        if p is None:
            return None
        
        if p.left is not None:
            p = p.left
            while p.right is not None:
                p = p.right
            return p
        
        node = root
        res = None
        while node != p:
            if p.val > node.val:
                res = node
                node = node.right
            else:
                node = node.left
        
        return res
        
        
            
        
        
        
        
        
        
        
        
                
                
        
        
        
        
        