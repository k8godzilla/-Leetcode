#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:15:48 2019

@author: sunyin
"""

'''
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def shortestDistance(self, words: list, word1: str, word2: str) -> int:
    # def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = (-1) * len(words), (-1) * len(words)
        dist = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
                dist = min(abs(i1 - i2), dist)
                if dist == 1:
                    return 1
            elif words[i] == word2:
                i2 = i
                dist = min(abs(i1 - i2), dist)
                if dist == 1:
                    return 1
        return dist
            

