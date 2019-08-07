# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:39:49 2019

@author: admin
"""

'''
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        # findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        idxEnd = -1
        self.beginWord = beginWord
        self.wordList = wordList
        for i in range(len(self.wordList)):
            if self.wordList[i] == endWord:
                idxEnd = i
                break
        if idxEnd == -1:
            return []
        
        if len(self.beginWord) == 1:
            if self.beginWord not in self.wordList:
                res = []
                for w in self.wordList:
                    if w != endWord:
                        res.append([self.beginWord, w, endWord])
                return res
            else:
                return [[self.beginWord, endWord]]
        
        
        # 按照位置上的字母录入单词
        
        self.wordsMega = []
        for i in range(len(wordList[0])):
            d = {}
            for j in range(len(wordList)):
                try:
                    d[wordList[j][i]].add(j)
                except:
                    d[wordList[j][i]] = set([j])
            self.wordsMega.append(d)
        
        
        self.path = []
        self.frontier = self.findNeighbours(beginWord)
        if idxEnd in self.frontier:
            return [[beginWord, endWord]]
        self.explore = set()
        self.explore.update(self.frontier)
        
        self.hq = {}
        for f in self.frontier:
            self.hq[f] = []
            
        endFound = False
        while len(self.frontier) > 0 and endFound == False:
            frontierNew = set()
            
            for f in self.frontier:
                nf = self.findNeighbours(self.wordList[f])
                nf = nf - self.explore
                for n in nf:
                    try:
                        self.hq[n].add(f)
                    except:
                        self.hq[n] = set([f])
                frontierNew.update(nf)
            if idxEnd in frontierNew:
                endFound = True
            self.explore.update(frontierNew)
            self.frontier = frontierNew
        
        if endFound == False:
            return []
        else:
            return self.searchPath(idxEnd)
    
    def searchPath(self, idx):
        if self.hq[idx] == []:
            return [[self.beginWord, self.wordList[idx]]]
        else:
            path = []
            for idxP in self.hq[idx]:
                pp = self.searchPath(idxP)
                for i in range(len(pp)):
                    pp[i].append(self.wordList[idx])
                path.extend(pp)
            return path
            
                
        
        
    def findNeighbours(self, word):
        ng = set()
        for i in range(len(word)):
            ngi = []
            suc = True
            for j in range(len(word)):
                if i != j:
                    try:
                        ngi.append(self.wordsMega[j][word[j]])
                    except:
                        suc = False
                        break
            if suc:
                ni = ngi[0]
                for j in range(1, len(ngi)):
                    ni = ni.intersection(ngi[j])
                ng.update(ni)
        return ng
                
                
            

cl = Solution()

beginWord = "hot"
endWord = "dot"
wordList = ["dot","dog"]

res = cl.findLadders(beginWord, endWord, wordList)


hq = cl.hq


ng = cl.findNeighbours(beginWord)




