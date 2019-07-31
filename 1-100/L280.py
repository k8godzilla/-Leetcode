# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:41:17 2019

@author: admin
"""

'''
给你一个无序的数组 nums, 将该数字 原地 重排后使得 nums[0] <= nums[1] >= nums[2] <= nums[3]...。

示例:

输入: nums = [3,5,2,1,6,4]
输出: 一个可能的解答是 [3,5,1,6,2,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-sort
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def wiggleSort(self, nums: list) -> None:
        # wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i % 2 == 1:
                if nums[i] < nums[i - 1]:
                    cache = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = cache
            else:
                if nums[i] > nums[i - 1]:
                    cache = nums[i - 1]
                    nums[i - 1] = nums[i]
                    nums[i] = cache
        
cl = Solution()
import numpy as np
nums = np.random.randint(0, 1000, 1000).tolist()
cl.wiggleSort(nums)                 
                
check1 = []
check0 = []
for i in range(1, len(nums) - 1):
    if i % 2 == 1:
        if nums[i] < nums[i - 1] or nums[i] < nums[i + 1]:
            check1.append(i)
    else:
        if nums[i] > nums[i - 1] or nums[i] > nums[i + 1]:
            check0.append(i)
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
