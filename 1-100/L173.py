#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:45:44 2019

@author: sunyin
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path = []
        head = root
        while head is not None:
            self.path.append(head)
            head = head.left
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        head = self.path.pop()
        headRight = head.right
        while headRight is not None:
            self.path.append(headRight)
            headRight = headRight.left
        return head.val
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.path) == []:
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()