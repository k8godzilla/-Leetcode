#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:24:56 2019

@author: sunyin
"""

'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        
        if len(word) == 0:
            return False
        
        front0 = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    front0.add((i, j))
                    
        if len(front0) == 0:
            return False
        
        if len(word) == 1:
            return True
        
        self.board = board
        self.word = word
        
        self.row, self.col = len(board), len(board[0])

        
        
        self.ij_mem = set()
        layer = 0
        for ij in front0:
            res = self.searchNext(1, ij)
            if res:
                return True
        return False
            
            
    def searchNext(self, layer, ij):
        i, j = ij
        f = []
        self.explore(layer, i + 1, j, f)
        self.explore(layer, i - 1, j, f)
        self.explore(layer, i , j + 1, f)
        self.explore(layer, i , j - 1, f)
        print(i, j,layer, f)
        if len(f) > 0:
            if layer + 1 >= len(self.word):
                return True
            self.ij_mem.add(ij)
            for ij_f in f:
                res_next = self.searchNext(layer + 1, ij_f)
                if res_next:
                    return True
            self.ij_mem.remove(ij)
        return False
                
        
        
    
    def explore(self, layer, i, j, f):

        if i >= 0 and j >= 0 and i <= self.row - 1 and j <= self.col - 1:
            if self.board[i][j] == self.word[layer] and (i, j) not in self.ij_mem:
                f.append((i, j))

            else:
                pass


        
        