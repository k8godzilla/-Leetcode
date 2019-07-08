#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 07:42:08 2019

@author: sunyin
"""


'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def nextPermutation(self, nums) :
        
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_pointer = -1
        
        ### 从末端开始寻找前面的元素小于后面的元素的最后一个idx
        while True:
            try:
                if nums[idx_pointer] > nums[idx_pointer - 1]:
                    break
                else:
                    idx_pointer -= 1
            except:
                break
        
        ### 将大于nums[idx_left]的最右侧的元素和nums[idx_left]交换
        ### [2, 5, 4, 3, 1] -> [3, 5, 4, 2, 1]
        idx_left = len(nums) + idx_pointer - 1
        if idx_left >= 0:
            idx_right = -1
            while nums[idx_right] <= nums[idx_left]:
                idx_right -= 1
            cache = nums[idx_left]
            nums[idx_left] = nums[idx_right]
            nums[idx_right] = cache
        
        self.elementSwap(nums, idx_left + 1)
            
            
    ### 将i_start右侧（包含）的元素两两互换
    ### [3, 5, 4, 2, 1] , 1 -> [3, 1, 2, 4, 5]
    def elementSwap(self, nums, i_start):
        i_end = len(nums) - 1
        while i_start < i_end:
            cache = nums[i_start]
            nums[i_start] = nums[i_end]
            nums[i_end] = cache
            i_start += 1
            i_end -= 1
        
        
        



