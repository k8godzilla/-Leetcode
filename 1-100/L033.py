# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:41:06 2019

@author: admin
"""

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1


'''

class Solution:
    def search(self, nums, target):
        
        
        if len(nums) == 0:
            return -1
        
        i, j = 0, len(nums) - 1
        idx_split = -1
        
        
        ### 首先寻找翻转idx，利用binary method
        while i <= j:
            if j - i <= 1:
                ### 防止陷入死循环
                if nums[i - 1] > nums[0] and nums[i] < nums[0]:
                    idx_split = i
                    break
                else:
                    idx_split = j
                    break
            else:
                idx_middle = (i + j) // 2
                if nums[idx_middle - 1] > nums[0]:
                    if nums[idx_middle] < nums[0]:
                        idx_split = idx_middle
                        break
                    else:
                        i = idx_middle
                else:
                    j = idx_middle
        
        res = self.binarySearch(nums, target, 0, idx_split)
        if res != -1:
            return res
        else:
            return self.binarySearch(nums, target, idx_split, len(nums) - 1)

    
    def binarySearch(self, nums, target, i_start, i_end):
        ### 利用binary method寻找目标idx
        if i_end < i_start:
            return -1
        elif i_end == i_start:
            if nums[i_start] == target:
                return i_start
            else:
                return -1
        else:
            while i_start <= i_end:
                if i_end - i_start <= 1:
                    ### 防止陷入死循环
                    if nums[i_start] == target:
                        return i_start
                    elif nums[i_end] == target:
                        return i_end
                    else:
                        return -1
                else:
                    idx_middle = (i_start + i_end) // 2
                    if nums[idx_middle] == target:
                        return idx_middle
                    elif nums[idx_middle] < target:
                        i_start = idx_middle
                    else:
                        i_end = idx_middle
                
    

                