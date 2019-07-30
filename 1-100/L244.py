#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:25:47 2019

@author: sunyin
"""

'''
请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-word-distance-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class WordDistance:

    def __init__(self, words: list):
        # __init__(self, words: List[str]):
        self.wordsIdx = {}
        for i in range(len(words)):
            try:
                self.wordsIdx[words[i]].append(i)
            except:
                self.wordsIdx[words[i]] = [i]
        
        

    def shortest(self, word1: str, word2: str) -> int:
        idx1, idx2 = self.wordsIdx[word1], self.wordsIdx[word2]
        i, j = 0, 0
        dist = abs(idx1[0] - idx2[0])
        while i < len(idx1) and j < len(idx2):
            dist = min(dist, abs(idx1[i] - idx2[j]))
            if idx1[i] < idx2[j]:
                i += 1
            else:
                j += 1
        return dist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)