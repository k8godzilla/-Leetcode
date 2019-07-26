# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:43:25 2019

@author: admin
"""

'''
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
            
        if i > j:
            return s
        
        iStart = i
        iEnd = j
        
        print(iStart, iEnd)
        for i in range(iEnd, iStart - 1, -1):
            print(s[iStart:i])
            
            if self.isSym(s[iStart:i]):
                
                t = s[i:iEnd + 1]
                t = t[::-1]

                return s[:iStart] + t + s[iStart:]
            

    def isSym(self, s):
        if len(s) <= 1:
            return True
        i = (len(s) - 1) // 2
        j = len(s) // 2
        while i >= 0:
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1
        return True
    
  
    
cl = Solution()

s =  "aabba"

res = cl.shortestPalindrome(s)








