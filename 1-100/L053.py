#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:20:59 2019

@author: sunyin
"""

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 1
        sum_max = nums[0]
        sum_keep = nums[0]
        if sum_keep < 0:
            sum_keep = 0
        while i < len(nums):
            sum_keep += nums[i]
            if sum_keep > sum_max:
                sum_max = sum_keep
            if sum_keep < 0:
                sum_keep = 0
            i += 1
        return sum_max