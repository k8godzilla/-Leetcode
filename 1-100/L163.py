#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:54:25 2019

@author: sunyin
"""

'''
给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：

输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findMissingRanges(self, nums: list, lower: int, upper: int) -> list:
        # def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        

        
        
        if len(nums) == 0:
            if lower == upper:
                nums = [lower]
                return [str(lower)]
            else:
                nums = [lower - 1, upper + 1]
        else:
            if lower < nums[0]:
                nums = [lower - 1] + nums
            if upper > nums[-1]:
                nums.append(upper + 1)
            
        if len(nums) == 1:
            return []

        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 2:
                res.append(str(nums[i] - 1))
            elif nums[i] - nums[i - 1] > 2:
                start = str(nums[i - 1] + 1)
                end = str(nums[i] - 1)
                se = start + '->' + end
                res.append(se)
        return res
            
 
cl = Solution()
nums = [-1]
lower = -2
upper = 0
res = cl.findMissingRanges(nums, lower, upper)           
        
       
