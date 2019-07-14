#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:57:00 2019
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@author: sunyin
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        self.length_s = len(s)
        
        app_times = {}
        for i in range(len(t)):
            try:
                app_times[t[i]] += 1
            except:
                app_times[t[i]] = 1
        
        idx_mem = {}
        for i in range(len(t)):
            idx_mem[t[i]] = []
            
        self.res = (-1, len(s) + 1)    
        app = 0
        

        
        for i in range(len(s)):
            if app < len(app_times.keys()):
                if s[i] in idx_mem.keys():
                    idx_mem[s[i]].append(i)
                    if len(idx_mem[s[i]]) == app_times[s[i]]:
                        app += 1
                    elif len(idx_mem[s[i]]) > app_times[s[i]]:
                        idx_mem[s[i]] = idx_mem[s[i]][1:]
                if app == len(app_times.keys()):
                    self.subUpdate(idx_mem, i)
            else:
                if s[i] in idx_mem.keys():
                    idx_mem[s[i]].append(i)
                    idx_mem[s[i]] = idx_mem[s[i]][1:]
                    if s[i] == self.key_min:
                        self.subUpdate(idx_mem, i)
        if self.res[0] == -1:
            return ''
        else:
            return s[self.res[0]:self.res[1]]
                    
                    
    def subUpdate(self, idx_mem, i):
        self.idx_min = self.length_s
        for key in idx_mem.keys():
            if idx_mem[key][0] < self.idx_min:
                self.idx_min = idx_mem[key][0]
                self.key_min = key
        if i + 1 - self.idx_min  < self.res[1] - self.res[0]:
            self.res = (self.idx_min, i + 1)