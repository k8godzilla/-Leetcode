#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:35:15 2019

@author: sunyin
"""

'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def majorityElement(self, nums: list) -> int:
        # majorityElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        
        ct = len(nums) // 2
        count = {}
        for i in range(len(nums)):
            try:
                count[nums[i]] += 1
            except:
                count[nums[i]] = 1
            if count[nums[i]] > ct:
                return nums[i]
    