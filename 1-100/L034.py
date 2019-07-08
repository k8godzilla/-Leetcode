# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:23:56 2019

@author: admin
"""

'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

'''

class Solution:
    def searchRange(self, nums, target):
        ### nums : List[int]
        ### target : int
        ### return : List[int]
        
        ### 先排除掉三种不会成立的情况
        if len(nums) == 0:
            return [-1, -1]
        elif nums[0] > target:
            return [-1, -1]
        elif nums[-1] < target:
            return [-1, -1]
        else:
            if nums[0] == target:
                i_left = 0
            else:
                i_left = self.searchPoint(nums, target, 'left')
            if i_left == -1:
                return [-1, -1]
            else:
                i_right = self.searchPoint(nums, target, 'right')
                return [i_left, i_right]
            
    def searchPoint(self, nums, target, mode):
        i, j = 0, len(nums) - 1
        while i <= j:
            if j - i <= 1:
                ### 防止陷入死循环
                if nums[j] == target:
                    return j
                elif nums[i] == target:
                    return i
                else:
                    return -1
            else:
                ### binary search 
                i_middle = (i + j) // 2
                if mode == 'left':
                    if nums[i_middle - 1] < target:
                        if nums[i_middle] == target:
                            return i_middle
                        elif nums[i_middle] > target:
                            return -1
                        else:
                            i = i_middle
                    else:
                        j = i_middle
                elif mode == 'right':
                    if nums[i_middle + 1] > target:
                        if nums[i_middle] == target:
                            return i_middle
                        elif nums[i_middle] < target:
                            return -1
                        else:
                            j = i_middle
                    else:
                        i = i_middle
                    
                        
                        
                        

        


