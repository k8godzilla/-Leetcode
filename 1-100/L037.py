# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:09:43 2019

@author: admin
"""

'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

'''

class Solution:
    def solveSudoku(self, board):
        ### board : List[List[str]]
        """
        Do not return anything, modify board in-place instead.
        """
        
        size = 9
        self.board = board
        
        self.row_mem = []
        self.col_mem = []
        self.group_mem = []
        for i in range(size):
            self.row_mem.append(set())
            self.col_mem.append(set())
            self.group_mem.append(set())
        
        ### 向men中录入原始信息
        for i in range(size):
            for j in range(size):
                bij = board[i][j]
                if bij != '.':
                    self.row_mem[i].add(bij)
                    self.col_mem[j].add(bij)
                    self.group_mem[self.groupNum(i, j)].add(bij)
        
        ### 统计每个grid的可能性            
        num_total = set(list('123456789'))
        self.psb = {}
        for i in range(size):
            for j in range(size):
                bij = board[i][j]
                gp_num = self.groupNum(i, j)
                if bij == '.':
                    psb_ij = num_total - self.row_mem[i] - self.col_mem[j] - self.group_mem[gp_num]
                    self.psb[(i, j, gp_num)] = psb_ij
        
        ### 从0开始探索           
        self.explore(0)
                    
                    

        

    def explore(self, idx_key):
        key = list(self.psb.keys())[idx_key]
        psb = self.psb[key]
        i, j, g = key
        for p in psb:
            if self.checkValid(i, j, g,p):
                ### 如果下一个key超出范围 直接返回true
                if idx_key + 1 == len(list(self.psb.keys())):
                    return True
                elif self.explore(idx_key + 1):
                    return True
                else:
                    self.removeMem(i, j, g, p)

        return False
                
        ### 无效则从mem中抹掉信息 不用抹掉board信息 因为最后一次肯定是正确的       
    def removeMem(self, i, j, g, p):
        self.row_mem[i].remove(p)
        self.col_mem[j].remove(p)
        self.group_mem[g].remove(p)
            
        ### 检查在grid中填入p是否有效，有效则修改mem和board    
    def checkValid(self, i, j, g, p):
        if p in self.row_mem[i]:
            return False
        if p in self.col_mem[j]:
            return False
        if p in self.group_mem[g]:
            return False
        self.row_mem[i].add(p)
        self.col_mem[j].add(p)
        self.group_mem[g].add(p)
        self.board[i][j] = p
        return True
        
        
    
    def groupNum(self, i, j):
        return (i // 3) * 3 + j // 3
        
        
        
        
        
sudoku = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

cl = Solution()
cl.solveSudoku(sudoku)  
        
        

        
