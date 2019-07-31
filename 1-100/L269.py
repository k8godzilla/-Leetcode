# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 11:31:47 2019

@author: admin
"""

'''
现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。

假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。

您需要根据这个输入的列表，还原出此语言中已知的字母顺序。

示例 1：

输入:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

输出: "wertf"
示例 2：

输入:
[
  "z",
  "x"
]

输出: "zx"
示例 3：

输入:
[
  "z",
  "x",
  "z"
] 

输出: "" 

解释: 此顺序是非法的，因此返回 ""。
注意：

你可以默认输入的全部都是小写字母
假如，a 的字母排列顺序优先于 b，那么在给定的词典当中 a 定先出现在 b 前面
若给定的顺序是不合法的，则返回空字符串即可
若存在多种可能的合法字母顺序，请返回其中任意一种顺序即可

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def alienOrder(self, words: list) -> str:
    # def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        
        self.allab = set()
        for w in words:
            for i in range(len(w)):
                self.allab.add(w[i])
        
        self.f = {}
        self.b = {}
        
        
        for i in range(len(words) - 1):
            b, s1, s2 = self.wordCompare(words[i], words[i + 1])
            if b:
                try:
                    self.f[s1].add(s2)
                except:
                    self.f[s1] = set()
                    self.f[s1].add(s2)
                try:
                    self.b[s2].add(s1)
                except:
                    self.b[s2] = set()
                    self.b[s2].add(s1)
        res = ''       
        while True:
            g = self.generate()
            if g != '':
                res += g
            else:
                break
        
        if len(self.b.keys()) >= 1:
            return ''
        
        abRemain = ''
        for ab in self.allab:
            if ab not in res:
                abRemain += ab
        return res + abRemain
            
            
            
    def generate(self):
        for k in self.f.keys():
            if k not in self.b.keys():
                fk = self.f[k]
                for bk in fk:
                    self.b[bk].remove(k)
                    if len(self.b[bk]) == 0:
                        del self.b[bk]
                del self.f[k]
                return k
        return ''
        
        
        
    def wordCompare(self, word1, word2):
        if word1 == '' or word2 == '':
            return False, '', ''
        i = 0
        while i < len(word1) and i < len(word2):
            if word1[i] != word2[i]:
                return True, word1[i], word2[i]
            i += 1
        return False, '', '' 
        
        
        
        
        
cl = Solution()
d = [
  "z",
  "x"
]  
res = cl.alienOrder(d)        
       
        
        
        












