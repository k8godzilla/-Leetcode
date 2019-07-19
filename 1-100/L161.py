# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:23:50 2019

@author: admin
"""

'''
给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：

往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t
示例 1：

输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。
示例 2:

输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。
示例 3:

输入: s = "1203", t = "1213"
输出: true
解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) >= 2:
            return False
        
        if len(s) == 0:
            if len(t) == 0:
                return False
            if len(t) == 1:
                return True
            
        if len(t) == 0:
            if len(s) == 1:
                return True
            
        i, j = 0, 0
        dist = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if len(s) == len(t):
                    i += 1
                    j += 1
                    dist += 1
                elif len(s) > len(t):
                    i += 1
                    dist += 1
                else:
                    j += 1
                    dist += 1
                if dist >= 2:
                    return False
            else:
                i += 1
                j += 1
        
        
        if dist == 1:
            if i == len(s) and j == len(t):
                return True
            else:
                return False
        elif dist == 0:
            if i == len(s) and j == len(t):
                return False
            else:
                return True


        
cl = Solution()
s = 'a'
t = 'ac'

res = cl.isOneEditDistance(s, t)
     



