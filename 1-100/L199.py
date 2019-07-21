# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:18:59 2019

@author: admin
"""

'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if root  is not None:
            front = [root]
        else:
            front = []
        while front != []:
            res.append(front[-1].val)
            frontNext = []
            for i in range(len(front)):
                node = front[i]
                if node.left is not None:
                    frontNext.append(node.left)
                if node.right is not None:
                    frontNext.append(node.right)
            front = frontNext
        return res
            
            
            
            
            
            
            
        
        

