#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:54:09 2019

@author: sunyin
"""

'''
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mapping = {}
        for i in range(1, 27):
            mapping[ab[i - 1]] = i
        
        t = 1
        cols = 0
        for i in range(-1, (-1) * len(s) - 1, -1):
            c = mapping[s[i]]
            cols += c * t
            t *= 26
        return cols
    
cl = Solution()
res = cl.titleToNumber('ZY')
            
            
            
            
            
            
            