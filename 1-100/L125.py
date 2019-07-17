# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:44:16 2019

@author: admin
"""

'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def __init__(self):
        self.lookup = set()
        ab = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        for i in range(len(ab)):
            self.lookup.add(ab[i])
        
        
        
        
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pal = True
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and s[i] not in self.lookup:
                i += 1
            while j >= 0 and s[j] not in self.lookup:
                j -= 1
            if i >= j:
                break
            if s[i] != s[j]:
                pal = False
                break
            i += 1
            j -= 1
        return pal
    
    
cl = Solution()
s = ".,"
res = cl.isPalindrome(s)
        