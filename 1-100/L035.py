# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:07:21 2019

@author: admin
"""

'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

'''

class Solution:
    def searchInsert(self, nums, target):
        ### nums : List[int]
        ### target : int
        ### return : int
        
        
        
        if len(nums) == 0:
            return 0
        elif nums[0] >= target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            i, j = 0, len(nums) - 1
            while i < j:
                if j - i <= 1:
                    if nums[i] == target:
                        return i
                    else:
                        return i + 1
                else:
                    i_middle = (i + j) // 2
                    if nums[i_middle] == target:
                        return i_middle
                    elif nums[i_middle] < target:
                        i = i_middle
                    else:
                        j = i_middle
        
        
'''
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            midd = (left + right) // 2
            if nums[midd] < target: left = midd + 1 # insert left side
            else: right = midd - 1
        return leftv
'''
        
        
        
        
        
