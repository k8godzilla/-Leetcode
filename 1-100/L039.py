#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:27:26 2019

@author: sunyin
"""

'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


'''



class Solution:
    def combinationSum(self, cand, target):
        ### candidates : List[int]
        ### target : int
        ### return : List[List[int]]
        
        print(cand, target)
        if len(cand) == 0:
            return []
        
        if target < cand[0]:
            return []
        
        res = []
        for i in range(len(cand)):
            if cand[i] <= target:
                times = 0
                ct = cand[i] * times
                while ct <= target:
                    res_t = [cand[i]] * times
                    if ct == target:
                        res.append(res_t)
                    else:
                        res_next = self.combinationSum(cand[i + 1:], target - ct)
                        if len(res_next) != 0:
                            for j in range(len(res_next)):
                                res.append(res_t + res_next[j])
                    times += 1
                    ct = cand[i] * times
            else:
                break
        return res
        
        
        
cl = Solution()

candidates = [2,3, 5]
target = 8

res = cl.combinationSum(candidates, target)



