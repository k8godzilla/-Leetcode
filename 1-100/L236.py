# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:58:33 2019

@author: admin
"""

'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res, _, _ = self.helper(root, p, q)
        return res
    
    def helper(self, node: TreeNode, p: TreeNode, q: TreeNode):
        if node == p:
            if node.left is not None:
                r, bp, bq = self.helper(node.left, p, q)
                if bq == True:
                    return node, True, True
            if node.right is not None:
                r, bp, bq = self.helper(node.right, p, q)
                if bq == True:
                    return node, True, True
            
            return None, True, False
        
        elif node == q:
            if node.left is not None:
                r, bp, bq = self.helper(node.left, p, q)
                if bp == True:
                    return node, True, True
            if node.right is not None:
                r, bp, bq = self.helper(node.right, p, q)
                if bp:
                    return node, True, True
            
            return None, False, True
        
        else:
            bbp, bbq = 0, 0
            if node.left is not None:
                #print(node.left.val, p.val, q.val)
                r, bp, bq = self.helper(node.left, p, q)
                bbp += bp
                bbq += bq
                if r is not None:
                    return r, bp, bq
            if node.right is not None:
                r, bp, bq = self.helper(node.right, p, q)
                bbp += bp
                bbq += bq
                if r is not None:
                    return r, bp, bq
            if bbp and bbq:
                return node, bbp, bbq
            else:
                return None, bbp, bbq

            
node0 = TreeNode(3)
node1 = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(0)
node6 = TreeNode(8)               

node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

cl = Solution()
res = cl.lowestCommonAncestor(node0, node1, node2)



a = cl.helper(node0 ,node1, node2)