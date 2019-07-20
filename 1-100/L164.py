#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:43:43 2019

@author: sunyin
"""

'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maximumGap(self, nums: list) -> int:
        # maximumGap(self, nums: List[int]) -> int:
        
        self.nums = nums
        if len(nums) <= 1:
            return 0
        else:
            self.min, self.max = nums[0], nums[0]
            for i in range(1, len(nums)):
                self.min = min(self.nums[i], self.min)
                self.max = max(self.nums[i], self.max)
            
            if self.max == self.min:
                return 0
            
            self.diff = self.max - self.min
            self.groups = [[] for _ in range(len(self.nums))]
            for i in range(len(self.nums)):
                idx = int((self.nums[i] - self.min) / self.diff * (len(self.nums) - 1))
                self.groups[idx].append(self.nums[i])
                
            self.notNullGroups = []
            for i in range(len(self.groups)):
                if self.groups[i] != []:
                    self.notNullGroups.append(i)
            
            if len(self.notNullGroups) == len(self.nums):
                return (self.max - self.min) // (len(self.nums) - 1)
            

            self.maxDiff = 0
            self.idxDiff = {}
            for i in range(len(self.notNullGroups) - 1):
                idxDiff = self.notNullGroups[i + 1] - self.notNullGroups[i]
                self.idxDiff[self.notNullGroups[i]] = idxDiff
                self.maxDiff = max(self.maxDiff, idxDiff)
                
            
           
             
            res = 0
            for idx in self.idxDiff:
                if self.idxDiff[idx] >= self.maxDiff - 1:
                    nums0 = self.groups[idx]
                    nums1 = self.groups[idx + self.idxDiff[idx]]
                    max0 = self.min
                    for i in range(len(nums0)):
                        max0 = max(max0, nums0[i])
                    min1 = self.max
                    for i in range(len(nums1)):
                        min1 = min(min1, nums1[i])
                    res = max(res, min1 - max0)
            return res
            
            
            
cl = Solution()

import numpy as np

nums = [13684,13701,15157,2344,28728,16001,9900,7367,30607,5408,17186,13230,1598,9766,13083,27618,29065,9171,2470,20163,5530,20665,14818,4743,24871,27852,8129,4071,17488,30904,1548,16408,1734,17271,19880,22269,18738,30242,6679,19867,13781,4615,10049,28877,9323,5373,11381,18489,13654,14324,28843,27010,10232,31696,29708,3008,28769,30840,21172,28461,20522,8745,17590,27936,30368,30993,24416,17472]

res = cl.maximumGap(nums)            
            
            
            
groups = cl.groups                
                
          
                
num = np.sort(nums)
numDiff = np.diff(num)
            
            
            
            
            
        