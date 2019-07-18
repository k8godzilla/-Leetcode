#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:58:33 2019

@author: sunyin
"""


'''
给定一个字符串，逐个翻转字符串中的每个单词。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        self.wordsReverse = []
        
        wordOn = False
        for i in range(-1, (-1) * len(s) - 1, -1):
            if wordOn == False:
                if s[i] != ' ':
                    idxEnd = i + 1
                    wordOn = True
            else:
                if s[i] == ' ':
                    idxStart = i + 1
                    if idxEnd == 0:
                        self.wordsReverse.append(s[idxStart:])
                    else:
                        self.wordsReverse.append(s[idxStart:idxEnd])
                    wordOn = False
        if wordOn == True:
            if idxEnd == 0:
                self.wordsReverse.append(s[(-1) * len(s): ])
            else:
                self.wordsReverse.append(s[(-1) * len(s): idxEnd])
        
        res = ''
        if self.wordsReverse == []:
            return res
        for word in self.wordsReverse:
            res += (' ' + word)
        return res[1:]
            
cl = Solution()
s ="a good   example"
res = cl.reverseWords(s)


