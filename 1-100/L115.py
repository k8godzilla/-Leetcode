#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:20:02 2019

@author: sunyin
"""

'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:

输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    
        
        if len(s) < len(t):
            return 0
        
        self.dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in range(len(self.dp)):
            self.dp[i][0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] != t[j - 1]:
                    self.dp[i][j] = self.dp[i - 1][j]
                else:
                    self.dp[i][j] = self.dp[i - 1][j] + self.dp[i - 1][j - 1]
        print(self.dp)
        return self.dp[-1][-1]
                
                
        
cl = Solution()
       
S = "babgbag"
T = "bag"

res = cl.numDistinct(S, T)


dp = cl.dp


