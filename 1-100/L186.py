# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 09:03:04 2019

@author: admin
"""

'''
给定一个字符串，逐个翻转字符串中的每个单词。

示例：

输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
注意：

单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的
进阶：使用 O(1) 额外空间复杂度的原地解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseWords(self, s: list) -> None:
        # reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return s
        
        idxSpace = [i for i in range(len(s)) if s[i] == ' ']
        
        if len(idxSpace) == 0:
            return s
        
        idxSpace = [-1] + idxSpace + [len(s)]
        i, j = 1, len(idxSpace) - 2
        cacheI = self.strCache(s, idxSpace[i - 1] + 1, idxSpace[i])
        cacheJ = self.strCache(s, idxSpace[j] + 1,idxSpace[j + 1])
        while i <= j:
            if idxSpace[i] < len(s) - idxSpace[j]:
                s[len(s) - idxSpace[i]: len(s) - idxSpace[i] + len(cacheI)] = cacheI
                i += 1
                cacheI = self.strCache(s, idxSpace[i - 1] + 1, idxSpace[i])
            else:
                s[len(s) - idxSpace[j] - len(cacheJ)  -1:len(s) - idxSpace[j] - 1] = cacheJ
                j -= 1
                cacheJ = self.strCache(s, idxSpace[j] + 1,idxSpace[j + 1])
        print(cacheI, cacheJ)
        return s
    
    def strCache(self, s, iStart, iEnd):
        cache = []
        for i in range(iStart, iEnd):
            cache.append(s[i])
        return cache
    
    
cl = Solution()
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s = cl.reverseWords(s)
        
        
        
        
        
        
        
        
        
        
        
        
