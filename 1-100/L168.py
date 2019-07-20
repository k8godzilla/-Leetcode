#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:15:47 2019

@author: sunyin
"""

'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def convertToTitle(self, n: int) -> str:
        cols = []
        alphabeta = 'zabcdefghijklmnopqrstuvwxy'
        alphabeta = alphabeta.upper()
        mapping = {}
        for i in range(26):
            mapping[i] = alphabeta[i]
        while n > 0:
            res = n % 26
            cols.append(mapping[res])
            if res == 0:
                res = 26
            n = (n - res) // 26
        cols.reverse()
        
        return ''.join(cols)
            
        
        
cl = Solution()
res = cl.convertToTitle(701)        
        
        