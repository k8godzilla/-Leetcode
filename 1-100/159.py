# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:51:56 2019

@author: admin
"""

'''
给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

示例 1:

输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。
示例 2:

输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        
        self.s = s
        self.wordsKeepTwo = [s[0]]
        self.idxesKeepTwo = [0]
        self.maxLength = 0
        self.replace = False
        self.idxRecent = 0
        
        
        for i in range(1, len(s)):
            self.updateOne(i)
            if len(self.wordsKeepTwo) == 2:
                break
            
        if len(self.wordsKeepTwo) == 1:
            return len(s)
        else:
            for j in range(i + 1, len(s)):
                self.updateTwo(j)
            return max(self.maxLength, len(s) - self.idxRecent )
            

        
    def updateOne(self, idx):
        if self.s[idx] in self.wordsKeepTwo:
            self.idxesKeepTwo[0] = idx
        else:
            self.wordsKeepTwo.append(self.s[idx])
            self.idxesKeepTwo.append(idx)

        
        
    def updateTwo(self, idx):
        if self.s[idx] in self.wordsKeepTwo:
            for i in range(2):
                if self.s[idx] == self.wordsKeepTwo[i]:
                    self.idxesKeepTwo[i] = idx
                    break
        else:
            self.maxLength = max(self.maxLength, idx - self.idxRecent)
            #print(self.maxLength, self.s[idx], self.idxesStartKeepTwo)
            if self.idxesKeepTwo[0] < self.idxesKeepTwo[1]:
                idxDelete = 0
            else:
                idxDelete = 1
            self.idxRecent = self.idxesKeepTwo[idxDelete] + 1
            del self.wordsKeepTwo[idxDelete]
            del self.idxesKeepTwo[idxDelete]

            self.wordsKeepTwo.append(self.s[idx])
            self.idxesKeepTwo.append(idx)

                
            
            
cl = Solution()            
s = "eceb"
res = cl.lengthOfLongestSubstringTwoDistinct(s)        
        
    


wk = cl.wordsKeepTwo



maxl = cl.maxLength