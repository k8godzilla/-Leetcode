# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:22:11 2019

@author: admin
"""

'''
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

'''

class Solution:
    def minDistance(self, word1, word2):
        # word1 : str
        # word2 : str
        # return : int
        
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        m, n = len(word1), len(word2)
        
        # 因为要考虑word是‘’的情况，所以dp要建成m + 1, n + 1
        self.dp = []
        for i in range(m + 1):
            self.dp.append([0] * (n + 1))
            
        self.dp[0] = list(range(n + 1))
        for i in range(m + 1):
            self.dp[i][0] = i
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = self.dp[i][j -1]
                up = self.dp[i - 1][j]
                left_up = self.dp[i - 1][j - 1]
                #如果两个word最后一个字一样，那么就不用再加1步了
                if word1[i - 1] == word2[j - 1]:
                    left_up -= 1
                self.dp[i][j] = min(left, up, left_up) + 1
                
        return self.dp[m][n]
                
      
 
        
        
word1 = "zoologicoarchaeologist"
word2 = "zoogeologist"       
        
cl = Solution()

res = cl.minDistance(word1, word2)        
        
        
        
        
        
        
        
dp = cl.dp        
        
        
        
        
        
        
        
        
        
        












