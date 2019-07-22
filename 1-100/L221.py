# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:28:12 2019

@author: admin
"""

'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def maximalSquare(self, matrix: list) -> int:
        # maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        if len(matrix) == 1:
            return max(map(int, matrix[0]))
        if len(matrix[0]) == 1:
            col = [int(matrix[i][0]) for i in range(len(matrix))]
            return max(col)
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        
        
        dp[0] = list(map(int,matrix[0]))
        
        if 1 in dp[0]:
            squareMax = 1
        else:
            squareMax = 0
            
        if squareMax == 1:
            for i in range(m):
                dp[i][0] = int(matrix[i][0])
        else:
            for i in range(m):
                dp[i][0] = int(matrix[i][0])
                if dp[i][0] == 1:
                    squareMax = 1
            
        iRow, iCol = 1, 1
        
        while iRow < m and iCol < n:
            for j in range(iCol, n):
                if matrix[iRow][j] == '1':
                    dp[iRow][j] = min(dp[iRow - 1][j - 1], dp[iRow - 1][j], dp[iRow][j - 1]) + 1
                    squareMax = max(squareMax, dp[iRow][j])
            for i in range(iRow, m):
                if matrix[i][iCol] == '1':
                    dp[i][iCol] = min(dp[i - 1][iCol - 1], dp[i - 1][iCol], dp[i][iCol - 1]) + 1
                    squareMax = max(squareMax, dp[i][iCol])
            iRow += 1
            iCol += 1
        return squareMax * squareMax
                    
            
            
        
        
        
a = ['2', '3']

b = max(map(int, a))       
        
        
        
        
        
        
        
        
        
        
        
        
        

