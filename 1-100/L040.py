# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:11:50 2019

@author: admin
"""

'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

'''


class Solution:
    def combinationSum2(self, cand, target):
        ### cand: List[int]
        ### target: int
        ### return : List[List[int]]
        
        cand.sort()
        times_limit = {}
        
        if len(cand) == 0:
            return []
        
        if target < cand[0]:
            return []
        
        cand_mem = cand[0]
        count = 1
        cand_uq = []
        for i in range(1, len(cand)):
            if cand[i] == cand_mem:
                count += 1
            else:
                times_limit[cand_mem] = count
                cand_uq.append(cand_mem)
                cand_mem = cand[i]
                count = 1
        times_limit[cand_mem] = count
        cand_uq.append(cand_mem)
        

        
        res = []
        i = 0
        if cand_uq[i] <= target:
            times = 0
            ct = cand[i] * times
            while ct <= target and times <= times_limit[cand_uq[i]]:
                res_t = [cand_uq[i]] * times
                if ct == target:
                    res.append(res_t)
                else:
                    res_next = self.combinationSumWithoutSort(cand_uq[i + 1:], target - ct, times_limit)
                    if len(res_next) != 0:
                        for j in range(len(res_next)):
                            res.append(res_t + res_next[j])
                times += 1
                ct = cand[i] * times

        return res
    
    def combinationSumWithoutSort(self, cand, target, times_limit):
        ### candidates : List[int]
        ### target : int
        ### return : List[List[int]]
        

        
        if len(cand) == 0:
            return []
        
        if target < cand[0]:
            return []
        
        res = []
        i = 0
        if cand[i] <= target:
            times = 0
            ct = cand[i] * times
            while ct <= target and times <= times_limit[cand[i]]:
                res_t = [cand[i]] * times
                if ct == target:
                    res.append(res_t)
                else:
                    res_next = self.combinationSumWithoutSort(cand[i + 1:], target - ct, times_limit)
                    if len(res_next) != 0:
                        for j in range(len(res_next)):
                            res.append(res_t + res_next[j])
                times += 1
                ct = cand[i] * times
        return res 
                        
                
                
                
cl = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8            
                
res = cl.combinationSum2(candidates, target)                
                
                
                
                
                
                
                
                
                
                
                
                
            
















