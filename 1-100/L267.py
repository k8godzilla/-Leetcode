#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:00:49 2019

@author: sunyin
"""

'''
给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。

如不能形成任何回文排列时，则返回一个空列表。

示例 1：

输入: "aabb"
输出: ["abba", "baab"]
示例 2：

输入: "abc"
输出: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution:
    def generatePalindromes(self, s: str) -> list:
    # def generatePalindromes(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        
        d = {}
        dDouble = {}
        for i in range(len(s)):
            try:
                d[s[i]] += 1
            except:
                d[s[i]] = 1
        
        sa = []
        for k in d.keys():
            if d[k] % 2 == 1:
                sa.append(k)
                
                if len(sa) > 1:
                    return []

            dDouble[k] = d[k] // 2
        
        comb = self.generateWords(dDouble)

        res = []
        for c in comb:
            c0 = ''.join(c)
            c.reverse()
            c1 = ''.join(sa)
            c2 = ''.join(c)
            res.append(c0 + c1 + c2)
        return res
        
        
    def generateWords(self, d):
        if sum(d.values()) == 1:
            for k in d.keys():
                if d[k] == 1:
                    return [[k]]
        res = []
        for k in d.keys():
            if d[k] >= 1:
                d[k] -= 1
                comb = self.generateWords(d)
                d[k] += 1
                for c in comb:
                    c.append(k)
                    res.append(c)
        return res
            
        



cl = Solution()
s = 'aaccbb'
res = cl.generatePalindromes(s)
