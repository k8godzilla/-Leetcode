# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:53:58 2019

@author: admin
"""

class Solution:
    def __init__(self):
        # 需要设置预存 否则重复计算太多 会超出时间限制
        self.treeCache = {}
        
    def numTrees(self, n):
        # n : int
        # return : int
        if n == 0:
            return 1
        elif  n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            combs = 0
            for i in range(n):
                try:
                    left = self.treeCache[i]
                except:
                    left = self.numTrees(i)
                    self.treeCache[i] = left
                try:
                    right = self.treeCache[n - 1 -i]
                except:
                    right = self.numTrees(n - 1 - i)
                    self.treeCache[n - 1 - i] = right
                combs += left * right
            return combs
        

cl = Solution()
res = cl.numTrees(19)
        
        