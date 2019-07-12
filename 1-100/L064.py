# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:34:30 2019

@author: admin
"""

'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。


'''

class Solution:
    def minPathSum(self, grid):
        # grid : List[List[int]]
        # return : int
        
        if len(grid) == 0:
            return 0
        
        self.row, self.col = len(grid), len(grid[0])
        
        if self.row == 1 and self.col == 1:
            return grid[0][0]
        
        
        step_mem = []
        for i in range(self.row):
            step_mem.append([0] * self.col)
        step_mem[-1][-1] = grid[-1][-1]
        
        frontier = set()
        if self.row - 2 >= 0:
            frontier.add((self.row - 2, self.col - 1))
        if self.col - 2 >= 0:
            frontier.add((self.row - 1, self.col - 2))
            
        while len(frontier) != 0:
            front_new = set()
            for f in frontier:
                i, j = f
                if i + 1 <= self.row - 1 and j + 1 <= self.col - 1:
                    step_mem[i][j] = min(step_mem[i + 1][j], step_mem[i][j + 1]) + grid[i][j]
                elif i + 1 <= self.row - 1:
                    step_mem[i][j] = step_mem[i + 1][j] + grid[i][j]
                else:
                    step_mem[i][j] = step_mem[i][j + 1] + grid[i][j]
                if i - 1 >= 0:
                    front_new.add((i - 1, j))
                if j - 1 >= 0:
                    front_new.add((i, j - 1))
            frontier = front_new
            
        return step_mem[0][0]
            
            
            
cl = Solution()        

grid = [[1,3,1],[1,5,1],[4,2,1]]    
        
res = cl.minPathSum(grid)       
        
        
        
        
        
        
        
        
        
        




















