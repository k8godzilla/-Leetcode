# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:08:00 2019

@author: admin
"""

'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # board: List[List[str]]
        self.board = board
        self.m = len(board)
        if self.m > 0:
            self.n = len(board[0])
            if self.n > 0:            
                self.oBound = set()
                for j in range(self.n):
                    if self.board[0][j] == 'O' and (0, j) not in self.oBound:
                        self.search(0, j)
                    if self.board[self.m - 1][j] == 'O' and (self.m - 1, j) not in self.oBound:
                        self.search(self.m - 1, j)
                for i in range(1, self.m - 1):
                    if self.board[i][0] == 'O' and (i, 0) not in self.oBound:
                        self.search(i, 0)
                    if self.board[i][self.n - 1] == 'O' and (i, self.n - 1) not in self.oBound:
                        self.search(i, self.n - 1)
                
                for i in range(1, self.m - 1):
                    for j in range(1, self.n - 1):
                        if board[i][j] == 'O' and (i, j) not in self.oBound:
                            board[i][j] = 'X'
                    
        
    
    def search(self, i, j):
        
        self.oBound.add((i, j))
        front = self.neighbourValid(i, j)
        while len(front) > 0:
            front_next = []
            for idx in front:
                self.oBound.add(idx)
                idx_next = self.neighbourValid(idx[0], idx[1])
                front_next.extend(idx_next)
            front = set(front_next)
            
        
        
    def neighbourValid(self,i, j):
        front = []
        if self.isValid(i + 1, j):
            front.append((i + 1, j))
        if self.isValid(i - 1, j):
            front.append((i - 1, j))
        if self.isValid(i, j + 1):
            front.append((i, j + 1))
        if self.isValid(i, j - 1):
            front.append((i, j - 1))
        return front
        
    def isValid(self, i, j):
        if i >= 0 and i < self.m:
            if j >= 0 and j < self.n:
                if self.board[i][j] == 'O':
                    if (i, j) not in self.oBound:
                        return True
        return False
        
        
cl = Solution()
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
cl.solve(board)

        
        
        
        
        
        
        
        
        
        

