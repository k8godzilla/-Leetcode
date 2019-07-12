# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:45:58 2019

@author: admin
"""

'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        idx = -1
        len_last = 0
        ### 从尾部开始遍历，如果s[idx]是空格，并且最长长度不为0，则此时最长长度就是答案。
        while idx >= (-1) * len(s):
            if s[idx] != ' ':
                len_last += 1
            else:
                if len_last > 0:
                    break
            idx -= 1
                
        return len_last
    
cl = Solution()
s = "Hello World"
res = cl.lengthOfLastWord(s)
        















