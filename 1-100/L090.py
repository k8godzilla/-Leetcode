#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:10:53 2019

@author: sunyin
"""


class Solution:
    def subsetsWithDup(self, nums):
        # nums : List[int]
        # return : List[List[int]]
        if len(nums) == 0:
            return [[]]
        
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        # 数据排序
        nums.sort()
        
        # 存入unique num和每个uniqe num的出现次数
        nums_uniq = []
        nums_count = []
        n_mem= nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == n_mem:
                count += 1
            else:
                nums_uniq.append(n_mem)
                nums_count.append(count)
                n_mem = nums[i]
                count = 1
        nums_uniq.append(n_mem)
        nums_count.append(count)
        
        return  self.buildSubSet(nums_uniq, nums_count)
        
    def buildSubSet(self, nums_uniq, nums_count):
        # 递归构建
        # 单一数字的话直接返回
        # 超过一个数字的话先去掉最小一个数字 然后求子集
        # 然后将最小的数字和求得的仔鸡组合
        if len(nums_uniq) == 1:
            subset = []
            for i in range(nums_count[0] + 1):
                subset.append([nums_uniq[0]] * i)
            return subset
        else:
            sub_old = self.buildSubSet(nums_uniq[1:], nums_count[1:])
            subset = []
            for i in range(nums_count[0] + 1):
                base = [nums_uniq[0]] * i
                for so in sub_old:
                    subset.append(base + so)
            return subset
            

cl = Solution()
nums = [0, 0, 1, 2, 2]
res = cl.subsetsWithDup(nums)        
        
