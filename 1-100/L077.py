#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:09:33 2019

@author: sunyin
"""

'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def combine(self, n, k):
        # n : int
        # k : int
        # return : List[List[int]]
        if k > n:
            return []
        
        return self.combineSub(1, n, k)
        
    def combineSub(self, n_start, n_end, k):
        print(n_start, n_end, k)
        if k == 1:
            res_sub = []
            for v in range(n_start, n_end + 1):
                res_sub.append([v])
            return res_sub
        if n_end - n_start + 1 < k:
            return []
        elif n_end - n_start + 1 == k:
            return [list(range(n_start, n_end + 1))]
        else:
            res_sub = []
            for v in range(n_start, n_end + 2 - k):
                if v <= n_end:
                    rv = self.combineSub(v + 1, n_end, k - 1)
                    if rv != []:
                        for r in rv:
                            res_sub.append([v] + r)
            return res_sub
    
            
            
        
        
