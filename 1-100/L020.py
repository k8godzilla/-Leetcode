#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:22:26 2019

@author: sunyin
"""

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        s : str
        return : bool
        '''
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        left = {'(','{','['}
        right_mapping = {')':'(',']':'[','}':'{'}
        cache = []
        for i in range(len(s)):
            si = s[i]
            if si in left:
                cache.append(si)
            else:
                try:
                    mem = cache.pop()
                    if right_mapping[si] != mem:
                        return False
                except:
                    return False
        if len(cache) > 0:
            return False
        else:
            return True
                






