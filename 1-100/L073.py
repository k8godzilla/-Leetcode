#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:27:35 2019

@author: sunyin
"""

'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？


'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.m, self.n = len(matrix), len(matrix[0])
        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] == 0:
                    self.setZerosIdx(matrix, i, j)
        
        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] == 'z':
                    matrix[i][j] = 0
        
        
    
    def setZerosIdx(self, matrix, i_z, j_z):
        # 通过把原本修改的格子改成z来避免重复转化
        for j in range(0, self.n):
            # 不能把原本是0的格子改成z
            if matrix[i_z][j] != 0:
                matrix[i_z][j] = 'z'
        for i in range(0, self.m):
            if matrix[i][j_z] != 0:
                matrix[i][j_z] = 'z'






