#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 07:45:21 2019

@author: sunyin
"""

'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        
        res = []
        while nums != []:
            nums_c = []
            for i in range(len(nums)):
                nums_c.append(nums[i])
            res.append(nums_c)
            nums = self.numsNext(nums)


        return res
            
        
        
    def numsNext(self, nums):
        change = False
        for i in range(len(nums) - 1):
            if nums[-2-i] < nums[-1-i]:
                change = True
                idx_left = -2 -i
                break

        if change:
            for i in range(len(nums) - 1):
                if nums[-1 -i] > nums[idx_left]:
                    idx_right = -1 - i
                    break
            cache = nums[idx_left]
            nums[idx_left] = nums[idx_right]
            nums[idx_right] = cache
            
            i, j = idx_left + 1, -1
            while i < j:
                cache = nums[i]
                nums[i] = nums[j]
                nums[j] = cache
                i += 1
                j -= 1
            return nums
        else:
            return []
            
cl = Solution()

nums = [1, 1, 2]

res = cl.permuteUnique(nums)

n = [1, 1, 2]
nn = cl.numsNext(n)

c = n
a.append(c)
n[0] = 100