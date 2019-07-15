# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:07:01 2019

@author: admin
"""

'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 首先把inorder上的顺序存成字典
        # 从前序遍历序列开始 参照中序遍历开始逐个节点处理
        # 每个新加的节点除了本身的值以外 还需要存储它的left和right可能的inorder取值范围
        
        
        if not preorder:
            return None
        if len(preorder) == 1:
            pass
            
        inorder_idx = {}
        for i in range(len(inorder)):
            inorder_idx[inorder[i]] = i
        
        tree_list = []
        
        root = TreeNode(preorder[0])
        tree_list.append([root, -1, len(preorder)])
        idx = 1
        while idx < len(preorder):
            node_i = TreeNode(preorder[idx])
            j = idx - 1
            while j >= 0:
                if inorder_idx[node_i.val] > tree_list[j][1] and  inorder_idx[node_i.val] < tree_list[j][2]:
                    if inorder_idx[node_i.val] < inorder_idx[tree_list[j][0].val]:
                        tree_list[j][0].left = node_i
                        # 如果一个节点是其上级的左节点 那么它的子节点的范围是其上一层节点的左侧子边界和上侧边界本身的inorder
                        tree_list.append([node_i, tree_list[j][1], inorder_idx[tree_list[j][0].val]])
                        break
                    if inorder_idx[node_i.val] > inorder_idx[tree_list[j][0].val]:
                        tree_list[j][0].right = node_i
                        # 如果一个节点是其上级的右节点 那么它的子节点的范围是上侧边界本身的inorder和上一层节点的右侧子边界
                        tree_list.append([node_i, inorder_idx[tree_list[j][0].val], tree_list[j][2]])
                        break
                j -= 1
            idx += 1
        return root
            
            
            

            
        
        
        
        
        
        
        
        
        
        
        
        