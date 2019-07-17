# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:17:09 2019

@author: admin
"""

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    
    def wordBreak(self, s: str, wordDict: list) -> bool:
        # wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordMaxLength = 0
        self.wordMemo = set()
        self.wordDict = set(wordDict)
        for word in wordDict:
            self.wordMaxLength = max(self.wordMaxLength, len(word))
        
        return self.forwardAttempt(s)
        
        
    def forwardAttempt(self, s):

        if len(s) == 0:
            return True
        idx = 1

        while idx <= min(len(s), self.wordMaxLength + 1):

            if s[:idx] in self.wordDict and s[idx:] not in self.wordMemo:
                isBreakable = self.forwardAttempt(s[idx:])
                if isBreakable:
                    return isBreakable
                else:
                    self.wordMemo.add(s[idx:])
            idx += 1
        return False
            
            
        
        
        
        
        
cl = Solution()        
s = "applepenapple"
wordDict = ["apple", "pen"]    
        
        
res = cl.wordBreak(s, wordDict)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        