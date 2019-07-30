#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:13:45 2019

@author: sunyin
"""

'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。f
'''



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if len(s) == 0 and len(t) == 0:
            return True
        
        d = {}
        for i in range(len(s)):
            try:
                d[s[i]] += 1
            except:
                d[s[i]] = 1
                
        for i in range(len(t)):
            try:
                d[t[i]] -= 1
                if d[t[i]] < 0:
                    return False
            except:
                return False
            
        return True
