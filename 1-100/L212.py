# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:10:43 2019

@author: admin
"""

'''
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findWords(self, board: list, words: list) -> list:
        # findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0:
            return 0
        if len(board[0]) == 0:
            return 0
        if len(words) == 0:
            return 0
        
        self.firstCharacter = {}
        for w in words:
            try:
                self.firstCharacter[w[0]].append(w)
            except:
                self.firstCharacter[w[0]] = [w]
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        







