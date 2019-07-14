#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:14:09 2019

@author: sunyin
"""

'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maximalRectangle(self, matrix):
        # matrix: List[List[str]]
        # return: int
        
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        
        group_total = self.colRead(matrix, 0)
        self.area_max = 0
        for g in group_total:
            area = (g[1] - g[0] + 1) * (1 - g[2])
            self.area_max = max(self.area_max, area)
            
            
        for j in range(1, len(matrix[0])):
            group_j = self.colRead(matrix, j)

            group_total = self.groupCombine(group_total, group_j, j)

            
        for g in group_total:
            area = (g[1] - g[0] + 1) * (len(matrix[0]) - g[2])
            self.area_max = max(self.area_max, area)
        return self.area_max
        
        
            
    def groupCombine(self, group_total, group_j, j):
        g_new = []
        for gt in group_total:
            for gj in group_j:
                if gt[0] > gj[1]:
                    pass
                else:
                    row_upper = max(gt[0], gj[0])
                    row_bottom = min(gt[1], gj[1])
                    
                    if row_upper <= row_bottom:
                        g_new.append([row_upper, row_bottom, gt[2]])
        group_j.extend(g_new)
        for g in group_j:
            area = (g[1] - g[0] + 1) * (j + 1 - g[2])
            self.area_max = max(self.area_max, area)
        return group_j
            
        
      
    def colRead(self, matrix, j):
        groups = []
        group_sub = []
        for i in range(len(matrix)):
            if matrix[i][j] == '1':
                group_sub.append(i)
            if matrix[i][j] == '0':
                if len(group_sub) != 0:
                    groups.append([group_sub[0], group_sub[-1], j])
                    group_sub = []
        if len(group_sub) != 0:
            groups.append([group_sub[0], group_sub[-1], j])
        return groups
    
cl = Solution()
matrix = [["0","0","0","1","0","1","1","1"],["0","1","1","0","0","1","0","1"],["1","0","1","1","1","1","0","1"],["0","0","0","1","0","0","0","0"],["0","0","1","0","0","0","1","0"],["1","1","1","0","0","1","1","1"],["1","0","0","1","1","0","0","1"],["0","1","0","0","1","1","0","0"],["1","0","0","1","0","0","0","0"]]
res = cl.maximalRectangle(matrix)
            







