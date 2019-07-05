# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:10:45 2019

@author: admin
"""

'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findSubstring(self, s, words):
        ### s : str
        ### words : List[str]
        ### return : List[int]
        res = []
        if len(words) == 0:
            return res
        step_size = len(words[0])
        words_count = {}
        for w in words:
            try:
                words_count[w] += 1
            except:
                words_count[w] = 1
        
        for idx_start in range(step_size):
            if idx_start + len(words) * step_size > len(s):
                break
            slide_count = {}
            for j in range(len(words)):
                try:
                    slide_count[s[idx_start + j * step_size: idx_start + (j + 1) * step_size]] += 1
                except:
                    slide_count[s[idx_start + j * step_size: idx_start + (j + 1) * step_size]] = 1
                    
            short_list = self.dict_compare_initial(words_count, slide_count)
            if len(short_list) == 0:
                res.append(idx_start)
            
            j = 0
            while idx_start + len(words) * step_size + (j + 1) * step_size <= len(s):
                word_remove = s[idx_start + j * step_size: idx_start + (j + 1) * step_size]
                word_add = s[idx_start + (len(words) + j) * step_size: idx_start + (len(words) + j + 1) * step_size]
                slide_count[word_remove] -= 1
                try:
                    slide_count[word_add] += 1
                except:
                    slide_count[word_add] = 1
                    
                short_list = self.dict_compare(words_count, slide_count, short_list, word_remove, word_add)
                if len(short_list) == 0:
                    res.append(idx_start + (j + 1) * step_size)
                j += 1
        return res
                
                ### dict compare
    
    def dict_compare_initial(self, words_count, slide_count):
        short_list = set()
        for key in words_count.keys():
            try:
                if slide_count[key] < words_count[key]:
                    short_list.add(key)
            except:
                short_list.add(key)
        return short_list
    
    def dict_compare(self, words_count, slide_count, short_list, word_remove, word_add):
        try:
            if words_count[word_remove] > slide_count[word_remove]:
                short_list.add(word_remove)
        except:
            pass
        try:
            if word_add in short_list and words_count[word_add] <= slide_count[word_add]:
                short_list.remove(word_add)
        except:
            pass
        return short_list
                
                    
            
cl = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best"]     
                    
res = cl.findSubstring(s, words)               

    

