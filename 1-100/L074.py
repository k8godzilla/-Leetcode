#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:50:50 2019

@author: sunyin
"""

'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        if len(matrix[0]) == 0:
            return False
        
        if target < matrix[0][0]:
            return False
        
         # 防止下一步的二叉寻找溢出
        if matrix[-1][0] <= target:
            i_m = -1
        else:   
            i_s, i_e = 0, len(matrix) - 1
            while i_s <= i_e:
                i_m = (i_s + i_e) // 2
                if target < matrix[i_m][0]:
                    i_e = i_m - 1
                elif target >= matrix[i_m + 1][0]:
                    i_s = i_m + 1
                else:
                    break
           
        i_s, i_e = 0, len(matrix[0]) - 1
        found = False
        while i_s <= i_e:
            i_mm = (i_s + i_e) // 2
            if target < matrix[i_m][i_mm]:
                i_e = i_mm - 1
            elif target > matrix[i_m][i_mm]:
                i_s = i_mm + 1
            else:
                found = True
                break
        
        return found