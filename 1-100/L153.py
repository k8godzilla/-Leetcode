#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:01:18 2019

@author: sunyin
"""

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findMin(self, nums: list) -> int:
        # findMin(self, nums: List[int]) -> int
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        else:
            if nums[-1] > nums[0]:
                return nums[0]
            i, j = 0, len(nums) - 1
            while i <= j:
                if j - i <= 1:
                    if nums[j - 1] > nums[j]:
                        return nums[j]
                    else:
                        return nums[i]
                i_m = (i + j) // 2
                if nums[i_m - 1] > nums[i_m]:
                    return nums[i_m]
                if nums[i_m] > nums[0]:
                    i = i_m + 1
                else:
                    j = i_m - 1

                
cl = Solution()
nums = [5,1,2,3,4]
res = cl.findMin(nums)                
                
                
                
                
