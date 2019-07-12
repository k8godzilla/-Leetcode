# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:42:12 2019

@author: admin
"""

'''
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


'''


class Solution:
    def fullJustify(self, words, maxWidth) :
        # words : List[str]
        # maxWidth : int
        # return : List[str]
        if len(words) == 0:
            return []
        self.maxw = maxWidth
        self.res = []
        self.idx_mem = 0
        idx = 1
        self.len_sub = len(words[0])
        while idx < len(words):
            wi = words[idx]
            if self.len_sub + len(wi) + 1 > maxWidth:
                self.fillSub(idx, words)
            else:
                self.len_sub += len(wi) + 1
            idx += 1
        
        if self.idx_mem <= len(words) - 1:
            sub = ''
            for i in range(self.idx_mem, len(words)):
                sub += words[i]
                sub += ' '
        if len(sub) > self.maxw:
            sub = sub[:-1]
        else:
            sub = sub + ' ' * (self.maxw - len(sub))
        self.res.append(sub)
        
        return self.res
        
        
            
    def fillSub(self, idx, words):
        word_count = idx - self.idx_mem
        if word_count == 1:
            sub = words[self.idx_mem] + ' ' * (self.maxw - self.len_sub)
            self.res.append(sub)
        else:
            space_extra = self.maxw - self.len_sub
        
            a, b = space_extra // (word_count - 1), space_extra % (word_count - 1)
        
            sub = ''
            for i in range(self.idx_mem, idx):
                sub += words[i]
                if len(sub) < self.maxw:
                    sub += ' ' * (1 + a + 1 * ((i - self.idx_mem) < b))
            self.res.append(sub)
        self.len_sub = len(words[idx])
        self.idx_mem = idx
                
            
        
        
            
cl = Solution()
           
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]      
maxWidth = 20
res = cl.fullJustify(words, maxWidth)












