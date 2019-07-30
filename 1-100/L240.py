# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:50:16 2019

@author: admin
"""

'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False
        
        self.matrix = matrix
        self.target = target
        m, n = len(matrix) , len(matrix[0]) 
        
        
        if m == 1:
            iStart = 0
        else:       
            i0, i1 = 0, m - 1
            while i0 <= i1:
                if i1 - i0 <= 1:
                    if matrix[i1][0] <= target:
                        iStart = i1
                        break
                    else:
                        iStart = i0
                        break
                else:
                    iM = (i0 + i1) // 2
                    if matrix[iM][0] <= target and matrix[iM + 1][0] > target:
                        iStart = iM
                        break
                    elif matrix[iM][0] > target:
                        i1 = iM
                    else:
                        i0 = iM

            
        if n == 1:
            jEnd = 0
        else:
            j0, j1 = 0, n - 1
            while j0 <= j1:
    
                if j1 - j0 <= 1:
                    if matrix[0][j1] <= target:
                        jEnd = j1
                        break
                    else:
                        jEnd = j0
                        break
                else:
                    jM = (j0 + j1) // 2
                    if matrix[0][jM] <= target and matrix[0][jM + 1] > target:
                        jEnd = jM
                        break
                    elif matrix[0][jM] > target:
                        j1 = jM
                    else:
                        j0 = jM
                        

        
        i, j = iStart, 0
        while i >= 0 and j <= jEnd:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
                
            
            
            
cl = Solution()            
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]   

target = 22
res = cl.searchMatrix(matrix, target)         
            
            
            
            
            
            
                
                
        
        
        







